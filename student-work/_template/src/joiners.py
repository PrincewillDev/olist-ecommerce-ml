"""Step-by-step join functions for building the order-level Olist dataset.

Each function should take the current working table plus one raw (or
aggregated) table and return the merged result. Row-count checks belong to
the caller (see notebooks/02_join_tables.ipynb) with log_join_step, so each
join itself should stay a small, pure, independently testable transform.

Join order: orders -> customers -> order_items -> payments -> reviews ->
products/category_translation -> sellers.

Cardinality note: order_items and order_payments are NOT one-row-per-order
(see modules/module-4-data-preparation.md) — check row counts before and
after every join step. Don't assume order_reviews is safe just because it's
documented as one row per order; check that assumption against the real
data too before you trust it.
"""
import pandas as pd


def join_customers(orders: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    """Left-join customers onto orders on customer_id. Grain stays one row per order."""
    # TODO: implement
    raise NotImplementedError


def join_order_items(df: pd.DataFrame, order_items: pd.DataFrame) -> pd.DataFrame:
    """Left-join order_items onto the working table on order_id.

    order_items has multiple rows per order_id (one per line item), so this
    intentionally changes the table's grain to one row per order-item.
    """
    # TODO: implement
    raise NotImplementedError


def aggregate_payments(payments: pd.DataFrame) -> pd.DataFrame:
    """Collapse order_payments to one row per order_id before it gets joined.

    Think about why this needs to happen before the join, not after, given
    the table's grain at that point in the pipeline.
    """
    # TODO: implement
    raise NotImplementedError


def join_payments(df: pd.DataFrame, payments_agg: pd.DataFrame) -> pd.DataFrame:
    """Left-join the order-level payments aggregate onto the working table on order_id."""
    # TODO: implement
    raise NotImplementedError


def deduplicate_reviews(reviews: pd.DataFrame) -> pd.DataFrame:
    """Collapse order_reviews to one row per order_id before it gets joined.

    Keep the most recent row per order_id by review_creation_date.
    """
    # TODO: implement
    raise NotImplementedError


def join_reviews(df: pd.DataFrame, reviews: pd.DataFrame) -> pd.DataFrame:
    """Left-join reviews onto the working table on order_id.

    Expects `reviews` to already be one row per order_id — see
    deduplicate_reviews(), which the caller must run first.
    """
    # TODO: implement
    raise NotImplementedError


def join_products(
    df: pd.DataFrame, products: pd.DataFrame, category_translation: pd.DataFrame
) -> pd.DataFrame:
    """Attach English category names to products, then left-join products onto the working table on product_id."""
    # TODO: implement
    raise NotImplementedError


def join_sellers(df: pd.DataFrame, sellers: pd.DataFrame) -> pd.DataFrame:
    """Left-join sellers onto the working table on seller_id."""
    # TODO: implement
    raise NotImplementedError


def log_join_step(step_name: str, before_rows: int, after_rows: int) -> str:
    """Format a one-line row-count sanity check for a join step."""
    # TODO: implement
    raise NotImplementedError


def build_full_join(tables: dict) -> tuple[pd.DataFrame, list[str]]:
    """Run the full orders -> ... -> sellers join pipeline over a load_all()-shaped dict.

    Returns the final joined table and the row-count log for every step.
    """
    # TODO: implement
    raise NotImplementedError
