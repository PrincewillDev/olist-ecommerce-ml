---
name: olist-project-guide
description: Domain reference for the Olist Delivery Risk Prediction classroom project. Table meanings, join keys, known data issues, and the phase-by-phase definition of done. Use whenever working on joining, cleaning, exploring, or modeling this dataset.
---

# Olist Delivery Risk Prediction — Project Guide

## Dataset

[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## Tables and what one row means

| Table | One row is | Join key(s) |
| --- | --- | --- |
| olist_customers_dataset | one customer record | customer_id |
| olist_orders_dataset | one order | order_id, customer_id |
| olist_order_items_dataset | one product line item within one order (an order can have several) | order_id, product_id, seller_id |
| olist_order_payments_dataset | one payment installment/method entry for an order (an order can have more than one) | order_id |
| olist_order_reviews_dataset | one review for an order | order_id |
| olist_products_dataset | one product | product_id |
| olist_sellers_dataset | one seller | seller_id |
| olist_geolocation_dataset | one zip-code-prefix-level coordinate (many rows per prefix) | zip_code_prefix |
| product_category_name_translation | one Portuguese-to-English category name mapping | product_category_name |

## Known issues to check for, by phase

**Phase 2 (joins):** `order_items` and `order_payments` are not one-row-per-order. Joining either naively onto `orders` duplicates order-level fields. Always check row count before and after each join step.

**Phase 3 (cleaning):** decisions go in `student-work/<their-github-username>/docs/decision-log.md`.

- Missing `product_category_name` on some products, and some category names missing from the translation table.
- Missing review comments, this is expected, not every review has text.
- Delivery timestamps that occasionally predate purchase timestamps, worth flagging and inspecting, not silently dropping.
- Leakage: `review_score`, `review_comment_message`, `review_creation_date`, and `order_delivered_customer_date` are only known after delivery. None of these can be a *feature* if predicting anything at or before order/delivery time.
- Imbalance: review scores skew heavily toward 5 stars. The late-delivery label (once constructed) is also imbalanced, most orders arrive on time.

**Phase 6+ (modeling):** the late-delivery label is `order_delivered_customer_date > order_estimated_delivery_date`. Valid features are anything known at or before shipping time: product weight/dimensions, freight value, payment type/installments, customer/seller state, order item count. Anything from the reviews table, or the actual delivery date itself, is leakage.

## Definition of done, per phase

- **Phase 1:** one-sentence description of each table's grain, written down.
- **Phase 2:** joined table with a row-count sanity check documented at each join step.
- **Phase 3:** `student-work/<their-github-username>/docs/decision-log.md` has an entry for every missing-value, outlier, leakage, and categorical-handling decision made.
- **Phase 4-5:** at least 3 visualized relationships, each with a one-line written interpretation, plus a final EDA report.
- **Phase 6+:** a baseline model, an evaluated model using a metric appropriate to the imbalance (not raw accuracy), and an explicit statement of the leakage check performed.
