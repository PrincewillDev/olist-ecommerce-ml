from src.data_loader import TABLE_GRAINS, load_all


def test_table_grains_covers_every_loaded_table():
    tables = load_all()

    assert set(TABLE_GRAINS) == set(tables)


def test_load_all_returns_nonempty_dataframes():
    tables = load_all()

    for name, df in tables.items():
        assert len(df) > 0, f"{name} loaded empty"


def test_orders_has_expected_key_columns():
    tables = load_all()

    assert {"order_id", "customer_id", "order_purchase_timestamp"} <= set(tables["orders"].columns)
