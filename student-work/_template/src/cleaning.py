"""Cleaning functions for Phase 3: missing values, outliers, leakage, categorical data.

Each function should document *what* it does. The *why* behind each
decision belongs in decision-log.md, not in code comments.
"""
import pandas as pd

# Post-outcome fields: only known after delivery, so they can never be a
# *feature* for a model predicting anything at or before delivery time.
LEAKAGE_COLUMNS = [
    "order_delivered_customer_date",
    "review_score",
    "review_comment_message",
    "review_creation_date",
]


def fill_missing_category(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing product_category_name / product_category_name_english with 'unknown'."""
    # TODO: implement
    raise NotImplementedError


def flag_bad_delivery_timestamps(df: pd.DataFrame) -> pd.DataFrame:
    """Add a boolean column flagging rows where customer delivery predates purchase, without dropping them."""
    # TODO: implement
    raise NotImplementedError


def flag_bad_carrier_timestamps(df: pd.DataFrame) -> pd.DataFrame:
    """Add a boolean column flagging rows where carrier pickup predates purchase, without dropping them.

    Check this against flag_bad_delivery_timestamps() above — don't assume
    the two delivery-related date columns behave the same way on the real data.
    """
    # TODO: implement
    raise NotImplementedError


def assert_no_leakage(feature_columns: list[str]) -> None:
    """Raise ValueError if any known post-outcome leakage column is in the given feature list."""
    # TODO: implement
    raise NotImplementedError


def class_balance(series: pd.Series) -> pd.Series:
    """Return the proportion of each value in a categorical series, for reporting imbalance honestly."""
    # TODO: implement
    raise NotImplementedError
