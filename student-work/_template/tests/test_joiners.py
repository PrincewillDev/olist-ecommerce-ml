import pandas as pd

from src.joiners import (
    aggregate_payments,
    build_full_join,
    deduplicate_reviews,
    join_customers,
    join_order_items,
    join_payments,
    join_products,
    join_reviews,
    join_sellers,
    log_join_step,
)


def test_join_customers_preserves_order_grain():
    orders = pd.DataFrame({"order_id": ["o1", "o2"], "customer_id": ["c1", "c2"]})
    customers = pd.DataFrame({"customer_id": ["c1", "c2"], "customer_state": ["SP", "RJ"]})

    result = join_customers(orders, customers)

    assert len(result) == len(orders)
    assert "customer_state" in result.columns


def test_join_order_items_fans_out_to_item_grain():
    orders = pd.DataFrame({"order_id": ["o1", "o2"]})
    order_items = pd.DataFrame(
        {
            "order_id": ["o1", "o1", "o2"],
            "product_id": ["p1", "p2", "p3"],
            "seller_id": ["s1", "s1", "s2"],
        }
    )

    result = join_order_items(orders, order_items)

    assert len(result) == 3
    assert (result["order_id"] == "o1").sum() == 2


def test_aggregate_payments_collapses_to_one_row_per_order():
    payments = pd.DataFrame(
        {
            "order_id": ["o1", "o1", "o2"],
            "payment_value": [50.0, 50.0, 100.0],
            "payment_installments": [1, 2, 3],
            "payment_type": ["credit_card", "voucher", "boleto"],
        }
    )

    agg = aggregate_payments(payments)

    assert len(agg) == 2
    o1 = agg.loc[agg["order_id"] == "o1"].iloc[0]
    assert o1["payment_value_total"] == 100.0
    assert o1["payment_installments_max"] == 2
    assert o1["payment_type_count"] == 2


def test_join_payments_does_not_fan_out_a_second_time():
    # order-item-level table: o1 has 2 items, o2 has 1 item
    item_level = pd.DataFrame({"order_id": ["o1", "o1", "o2"], "product_id": ["p1", "p2", "p3"]})
    payments = pd.DataFrame(
        {
            "order_id": ["o1", "o1", "o2"],
            "payment_value": [50.0, 50.0, 100.0],
            "payment_installments": [1, 2, 1],
            "payment_type": ["credit_card", "voucher", "boleto"],
        }
    )
    payments_agg = aggregate_payments(payments)

    result = join_payments(item_level, payments_agg)

    # still one row per order-item, not multiplied by installment count
    assert len(result) == len(item_level)
    assert result.loc[result["order_id"] == "o1", "payment_value_total"].iloc[0] == 100.0


def test_deduplicate_reviews_keeps_most_recent_review_per_order():
    reviews = pd.DataFrame(
        {
            "order_id": ["o1", "o1", "o2"],
            "review_score": [3, 5, 4],
            "review_creation_date": ["2018-01-01", "2018-01-10", "2018-02-01"],
        }
    )

    result = deduplicate_reviews(reviews)

    assert len(result) == 2
    assert result.loc[result["order_id"] == "o1", "review_score"].iloc[0] == 5


def test_join_reviews_adds_review_columns():
    df = pd.DataFrame({"order_id": ["o1", "o2"]})
    reviews = pd.DataFrame({"order_id": ["o1", "o2"], "review_score": [5, 1]})

    result = join_reviews(df, reviews)

    assert list(result["review_score"]) == [5, 1]


def test_join_products_translates_category_name():
    df = pd.DataFrame({"product_id": ["p1"]})
    products = pd.DataFrame({"product_id": ["p1"], "product_category_name": ["cama_mesa_banho"]})
    category_translation = pd.DataFrame(
        {"product_category_name": ["cama_mesa_banho"], "product_category_name_english": ["bed_bath_table"]}
    )

    result = join_products(df, products, category_translation)

    assert result.loc[0, "product_category_name_english"] == "bed_bath_table"


def test_join_sellers_adds_seller_columns():
    df = pd.DataFrame({"seller_id": ["s1"]})
    sellers = pd.DataFrame({"seller_id": ["s1"], "seller_state": ["SP"]})

    result = join_sellers(df, sellers)

    assert result.loc[0, "seller_state"] == "SP"


def test_log_join_step_formats_row_counts():
    message = log_join_step("join_customers", 10, 10)

    assert message == "join_customers: 10 -> 10 rows"


def test_build_full_join_produces_item_level_grain_matching_order_items():
    tables = {
        "orders": pd.DataFrame({"order_id": ["o1", "o2"], "customer_id": ["c1", "c2"]}),
        "customers": pd.DataFrame({"customer_id": ["c1", "c2"], "customer_state": ["SP", "RJ"]}),
        "order_items": pd.DataFrame(
            {
                "order_id": ["o1", "o1", "o2"],
                "product_id": ["p1", "p2", "p3"],
                "seller_id": ["s1", "s1", "s2"],
            }
        ),
        "order_payments": pd.DataFrame(
            {
                "order_id": ["o1", "o1", "o2"],
                "payment_value": [50.0, 50.0, 100.0],
                "payment_installments": [1, 2, 1],
                "payment_type": ["credit_card", "voucher", "boleto"],
            }
        ),
        "order_reviews": pd.DataFrame(
            {
                "order_id": ["o1", "o2"],
                "review_score": [5, 1],
                "review_creation_date": ["2018-01-01", "2018-01-02"],
            }
        ),
        "products": pd.DataFrame(
            {"product_id": ["p1", "p2", "p3"], "product_category_name": ["toys", "toys", "books"]}
        ),
        "category_translation": pd.DataFrame(
            {"product_category_name": ["toys", "books"], "product_category_name_english": ["toys", "books"]}
        ),
        "sellers": pd.DataFrame({"seller_id": ["s1", "s2"], "seller_state": ["SP", "MG"]}),
    }

    result, log = build_full_join(tables)

    # grain stays at order_items level (3 rows), not fanned out further by payments
    assert len(result) == 3
    assert result.loc[result["order_id"] == "o1", "payment_value_total"].iloc[0] == 100.0
    assert len(log) == 7
