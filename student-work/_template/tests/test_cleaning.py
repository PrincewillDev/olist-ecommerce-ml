import pandas as pd
import pytest

from src.cleaning import (
    LEAKAGE_COLUMNS,
    assert_no_leakage,
    class_balance,
    fill_missing_category,
    flag_bad_carrier_timestamps,
    flag_bad_delivery_timestamps,
)


def test_fill_missing_category_replaces_nulls_with_unknown():
    df = pd.DataFrame(
        {
            "product_category_name": ["toys", None],
            "product_category_name_english": ["toys", None],
        }
    )

    result = fill_missing_category(df)

    assert result["product_category_name"].tolist() == ["toys", "unknown"]
    assert result["product_category_name_english"].tolist() == ["toys", "unknown"]


def test_fill_missing_category_does_not_mutate_input():
    df = pd.DataFrame({"product_category_name": [None]})

    fill_missing_category(df)

    assert df["product_category_name"].isna().all()


def test_flag_bad_delivery_timestamps_marks_delivery_before_purchase():
    df = pd.DataFrame(
        {
            "order_purchase_timestamp": pd.to_datetime(["2018-01-10", "2018-01-10"]),
            "order_delivered_customer_date": pd.to_datetime(["2018-01-05", "2018-01-15"]),
        }
    )

    result = flag_bad_delivery_timestamps(df)

    assert result["delivery_before_purchase"].tolist() == [True, False]


def test_flag_bad_carrier_timestamps_marks_carrier_before_purchase():
    df = pd.DataFrame(
        {
            "order_purchase_timestamp": pd.to_datetime(["2018-01-10", "2018-01-10"]),
            "order_delivered_carrier_date": pd.to_datetime(["2018-01-05", "2018-01-15"]),
        }
    )

    result = flag_bad_carrier_timestamps(df)

    assert result["carrier_before_purchase"].tolist() == [True, False]


def test_assert_no_leakage_raises_on_known_leakage_column():
    with pytest.raises(ValueError):
        assert_no_leakage(["freight_value", "review_score"])


def test_assert_no_leakage_passes_on_clean_feature_list():
    assert_no_leakage(["freight_value", "payment_value_total", "product_weight_g"])


def test_leakage_columns_match_documented_fields():
    assert set(LEAKAGE_COLUMNS) == {
        "order_delivered_customer_date",
        "review_score",
        "review_comment_message",
        "review_creation_date",
    }


def test_class_balance_sums_to_one():
    series = pd.Series([5, 5, 5, 1, 3])

    balance = class_balance(series)

    assert balance.sum() == pytest.approx(1.0)
    assert balance.loc[5] == pytest.approx(0.6)
