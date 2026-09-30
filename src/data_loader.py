"""
Loaders for the raw Olist Brazilian E-Commerce CSVs.

Each function loads exactly one CSV from data/ as-is —
no merging/joining happens here. Join logic belongs in a later,
dedicated step once each table has been explored on its own.
"""
import pandas as pd

from src.config import RAW_DATA_DIR


def load_customers() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_DIR / "olist_customers_dataset.csv")


def load_geolocation() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_DIR / "olist_geolocation_dataset.csv")


def load_order_items() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_DIR / "olist_order_items_dataset.csv")


def load_order_payments() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_DIR / "olist_order_payments_dataset.csv")


def load_order_reviews() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_DIR / "olist_order_reviews_dataset.csv")


def load_orders() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_DIR / "olist_orders_dataset.csv")


def load_products() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_DIR / "olist_products_dataset.csv")


def load_sellers() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_DIR / "olist_sellers_dataset.csv")


def load_category_translation() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA_DIR / "product_category_name_translation.csv")


def load_all() -> dict[str, pd.DataFrame]:
    """Load every raw table into a dict, keyed by table name. No joins."""
    return {
        "customers": load_customers(),
        "geolocation": load_geolocation(),
        "order_items": load_order_items(),
        "order_payments": load_order_payments(),
        "order_reviews": load_order_reviews(),
        "orders": load_orders(),
        "products": load_products(),
        "sellers": load_sellers(),
        "category_translation": load_category_translation(),
    }
