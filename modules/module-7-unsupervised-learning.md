# Module 7 — Unsupervised Learning (Optional / Bonus)

**This module is optional.** It is not required for the core project (Modules 4-6). Only attempt it once Modules 4-6 are done.

## Source

From `curriculum/artificial-intelligence-programme-guide.pdf`, Module 7: *Unsupervised Learning*:

> - Clustering, dimensionality reduction, anomaly detection, and segmentation
> - Evaluate groups without labelled answers
> - Build and explain a customer or operational segmentation project

Everything below **This project's application** translates that curriculum text into this project's optional extension. This is the "optionally compared against a customer-segmentation angle" mentioned as the bonus angle in [CLAUDE.md](../CLAUDE.md).

## This project's application

**The task (curriculum: "build and explain a customer or operational segmentation project").** Segment Olist customers using an RFM-style approach:

- **Recency** — time since a customer's most recent order.
- **Frequency** — number of orders per customer.
- **Monetary** — total (or average) amount spent per customer.

Compute these three values per customer from the Phase 2 joined table (`olist_customers_dataset`, `olist_orders_dataset`, `olist_order_payments_dataset`), then cluster customers on them (curriculum: "clustering").

**Evaluating without labels (curriculum: "evaluate groups without labelled answers").** There is no ground-truth "correct" segmentation here, unlike the labeled late-delivery problem in Modules 5-6. Evaluate cluster quality using unsupervised metrics (e.g. silhouette score) and, more importantly, by checking whether the resulting segments are *interpretable* — can you describe each cluster in a sentence a non-technical stakeholder would understand ("high-value repeat customers," "one-time low spenders")?

**Optional connection back to the core project.** If you want to go further, you can check whether delivery lateness (the Module 5/6 label) varies across the segments you find here — but this is an extension on top of the bonus, not a requirement of it.

**Leakage note.** The leakage rule from Module 4 (no `order_delivered_customer_date` or reviews-table fields as inputs) applies here too if you build features from order-level data — segmentation isn't exempt just because it's unsupervised.

## Definition of done (only if attempted)

- Per-customer Recency, Frequency, and Monetary values computed from the joined data.
- At least one clustering run over those features, with the number of clusters chosen deliberately (not arbitrarily) and that choice explained.
- A plain-language description of what each resulting segment represents.
- Any function under `src/` has at least a one-line docstring.
