"""Loaders for the raw Olist Brazilian E-Commerce CSVs.

Each function should load exactly one CSV from data/ as-is — no
merging/joining here. Join logic belongs in src/joiners.py, once each table
has been understood on its own (Phase 1) and only then combined (Phase 2).
"""
import pandas as pd

from src.config import RAW_DATA_DIR

# One-sentence grain description per table. Fill these in yourself as part
# of Phase 1 — what does one row in this table actually represent?
TABLE_GRAINS = {
    "customers": "TODO: one-sentence description of this table's grain",
    "orders": "TODO: one-sentence description of this table's grain",
    "order_items": "TODO: one-sentence description of this table's grain",
    "order_payments": "TODO: one-sentence description of this table's grain",
    "order_reviews": "TODO: one-sentence description of this table's grain",
    "products": "TODO: one-sentence description of this table's grain",
    "sellers": "TODO: one-sentence description of this table's grain",
    "geolocation": "TODO: one-sentence description of this table's grain",
    "category_translation": "TODO: one-sentence description of this table's grain",
}


def load_customers() -> pd.DataFrame:
    """Load olist_customers_dataset.csv as-is."""
    # TODO: implement
    raise NotImplementedError


def load_geolocation() -> pd.DataFrame:
    """Load olist_geolocation_dataset.csv as-is."""
    # TODO: implement
    raise NotImplementedError


def load_order_items() -> pd.DataFrame:
    """Load olist_order_items_dataset.csv as-is."""
    # TODO: implement
    raise NotImplementedError


def load_order_payments() -> pd.DataFrame:
    """Load olist_order_payments_dataset.csv as-is."""
    # TODO: implement
    raise NotImplementedError


def load_order_reviews() -> pd.DataFrame:
    """Load olist_order_reviews_dataset.csv as-is."""
    # TODO: implement
    raise NotImplementedError


def load_orders() -> pd.DataFrame:
    """Load olist_orders_dataset.csv as-is, parsing its date columns."""
    # TODO: implement
    raise NotImplementedError


def load_products() -> pd.DataFrame:
    """Load olist_products_dataset.csv as-is."""
    # TODO: implement
    raise NotImplementedError


def load_sellers() -> pd.DataFrame:
    """Load olist_sellers_dataset.csv as-is."""
    # TODO: implement
    raise NotImplementedError


def load_category_translation() -> pd.DataFrame:
    """Load product_category_name_translation.csv as-is."""
    # TODO: implement
    raise NotImplementedError


def load_all() -> dict[str, pd.DataFrame]:
    """Load every raw table into a dict, keyed by table name. No joins."""
    # TODO: implement
    raise NotImplementedError
