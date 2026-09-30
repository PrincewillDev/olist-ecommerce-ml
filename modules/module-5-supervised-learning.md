# Module 5 — Supervised Learning

## Source

From `curriculum/artificial-intelligence-programme-guide.pdf`, Module 5: *Supervised Learning*:

> - Regression, classification, baselines, and feature engineering
> - Train linear models, trees, ensembles, and nearest-neighbour models
> - Select suitable algorithms for a problem and dataset

Everything below **This project's application** translates that curriculum text into this project's specific classifier. Module 6 (evaluation) covers judging what you build here — this module is about building it.

## This project's application

This is the start of Phase 6+: building the late-delivery classifier.

**The prediction task.** This is a binary *classification* problem (curriculum: "classification"). The label is:

```
is_late = order_delivered_customer_date > order_estimated_delivery_date
```

This is the same label already defined in `.claude/skills/olist-project-guide/SKILL.md`. It is imbalanced — most orders arrive on time — which Module 6 covers when you evaluate the model, but it shapes how you should treat the baseline here too.

**Leakage rule (carried over from Module 4, restated because it's the most common mistake at this stage).** Only features known at or before shipping time are valid: product weight/dimensions, freight value, payment type/installments, customer/seller state, order item count, and similar. `order_delivered_customer_date` and anything from the reviews table (`review_score`, `review_comment_message`, `review_creation_date`) are not valid features — they are only known after the outcome you're predicting has already happened.

**Baseline first (curriculum: "baselines").** Before training anything, establish what a trivial baseline gets you — for example, always predicting "on time" (the majority class). Every model you build afterward should be compared against this number, not against nothing.

**Feature engineering (curriculum: "feature engineering").** Build features from the Phase 2 joined table: order item counts, total freight value, payment installment counts, and similar aggregates. Justify each feature against the leakage rule above before using it.

**Model selection (curriculum: "train linear models, trees, ensembles, and nearest-neighbour models" / "select suitable algorithms").** Train at least one real classifier beyond the baseline (e.g. logistic regression, a decision tree, or a random forest) and be able to explain *why* you picked it for this problem and this dataset — this is the curriculum's "select suitable algorithms" objective, not just "run a model."

## Definition of done

- A documented majority-class (or similarly trivial) baseline, with its score recorded.
- At least one trained classifier beyond the baseline.
- A short written justification of the algorithm choice, tied to the shape of this dataset (imbalance, feature types, size).
- Every feature used is checked against the Module 4 leakage rule, with that check stated explicitly (not just implied).
- Any function under `src/` has at least a one-line docstring.
