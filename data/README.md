# Data

This folder holds the raw Olist CSVs locally. They are not tracked in git — only this file and `.gitkeep` are.

## Getting the data

1. Download the dataset from Kaggle: [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
2. Extract the CSVs directly into this folder (`data/`), so you end up with:

```
data/
  olist_customers_dataset.csv
  olist_geolocation_dataset.csv
  olist_order_items_dataset.csv
  olist_order_payments_dataset.csv
  olist_order_reviews_dataset.csv
  olist_orders_dataset.csv
  olist_products_dataset.csv
  olist_sellers_dataset.csv
  product_category_name_translation.csv
```

No subfolders, no renaming — the loaders expect these exact filenames in this exact location.
