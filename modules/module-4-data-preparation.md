# Module 4 — Data Preparation and Exploration

## Source

From `curriculum/artificial-intelligence-programme-guide.pdf`, Module 4: *Data Preparation and Exploration*:

> - Load, clean, join, transform, and validate datasets with pandas
> - Handle missing values, outliers, leakage, imbalance, and categorical data
> - Explore relationships and communicate findings visually

Everything below the line marked **This project's application** translates that curriculum text into the specific scope of the Olist Delivery Risk Prediction project. The curriculum sets the *skills*; this document sets *what doing those skills looks like on this dataset*.

## This project's application

Module 4 covers Phases 0 through 5 of the project, as already defined in [CLAUDE.md](../CLAUDE.md) and `.claude/skills/olist-project-guide/SKILL.md`:

- **Phase 0-1 — Environment setup, understanding each raw table.** Curriculum: "load ... datasets with pandas." Project: load each of the nine raw Olist tables independently (no joins yet) and write a one-sentence description of what one row means in each table.
- **Phase 2 — Joining tables.** Curriculum: "join ... datasets with pandas." Project: build the joined order-level table. `olist_order_items_dataset` and `olist_order_payments_dataset` are not one-row-per-order — check and document row counts before and after every join step.
- **Phase 3 — Cleaning.** Curriculum: "handle missing values, outliers, leakage, imbalance, and categorical data." Project:
  - Missing values: `product_category_name` gaps, and category names missing from the translation table.
  - Outliers/anomalies: delivery timestamps that predate purchase timestamps — flag and inspect, don't silently drop.
  - Leakage: `order_delivered_customer_date`, `review_score`, `review_comment_message`, and `review_creation_date` are only known after delivery. None of these may be used as a *feature* for a model predicting anything at or before delivery time.
  - Imbalance: review scores skew heavily toward 5 stars; the late-delivery label (once constructed in Module 5/6) is also imbalanced. Report imbalance honestly — don't "fix" it by deleting majority-class rows without justifying what that does to the analysis.
- **Phase 4 — EDA and visualization.** Curriculum: "explore relationships and communicate findings visually." Project: at least 3 visualized relationships in the joined data, each with a one-line written interpretation.
- **Phase 5 — EDA report.** Curriculum: same exploration objective, packaged as a deliverable. Project: a short written report summarizing what Phases 0-4 found, referencing the visualizations from Phase 4.

## Definition of done

- Phase 1: one-sentence grain description for every raw table.
- Phase 2: joined table with a documented row-count sanity check at each join step.
- Phase 3: `docs/decision-log.md` (inside your `student-work/<your-github-username>/` folder) has an entry for every missing-value, outlier, leakage, and categorical-handling decision made.
- Phase 4: at least 3 visualized relationships, each with a one-line interpretation.
- Phase 5: a final EDA report summarizing the above.
- Any function under `src/` has at least a one-line docstring.
