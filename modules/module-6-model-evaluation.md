# Module 6 — Model Evaluation and Improvement

## Source

From `curriculum/artificial-intelligence-programme-guide.pdf`, Module 6: *Model Evaluation and Improvement*:

> - Train, validation, and test splits; cross-validation and pipelines
> - Accuracy, precision, recall, F1, ROC-AUC, and regression metrics
> - Tune models and diagnose underfitting, overfitting, bias, and variance

Everything below **This project's application** translates that curriculum text into judging the classifier built in Module 5.

## This project's application

This is the continuation of Phase 6+: evaluating the late-delivery classifier honestly.

**Splits (curriculum: "train, validation, and test splits").** Hold out a test set before touching any model. If you tune hyperparameters, use a validation split or cross-validation for that — never tune against the test set.

**The metric problem (curriculum: "accuracy, precision, recall, F1, ROC-AUC").** The late-delivery label is imbalanced (established in Module 4/5 — most orders arrive on time). Raw accuracy on an imbalanced label is misleading: a model that always predicts "on time" can score deceptively high accuracy while catching zero actual late deliveries. Pick a metric appropriate to the imbalance — precision, recall, F1, or ROC-AUC/PR-AUC — and be able to explain *why* that metric and not accuracy. This directly extends the imbalance guardrail already established in Module 4: reporting imbalance honestly doesn't stop at the data-cleaning stage, it has to carry into how you judge the model.

**Comparing against the baseline.** Report your chosen metric for both the Module 5 baseline and your trained classifier, side by side. "Better than the baseline" only means something if both are measured the same way.

**Diagnosis (curriculum: "diagnose underfitting, overfitting, bias, and variance").** State whether your model is over- or under-fitting (e.g. by comparing train vs. validation/test performance), and what you'd try next if you had more time — this doesn't need to be executed, just reasoned through.

**Leakage re-check.** Before calling evaluation done, restate explicitly that none of the features scored used `order_delivered_customer_date` or any reviews-table field. This is the same check from Module 4/5, repeated here because it's the last place to catch it before the numbers are reported.

## Definition of done

- A held-out test set that was not used for any tuning decision.
- A metric appropriate to the imbalance (not raw accuracy alone), reported for both the baseline and the trained classifier.
- A short over/underfitting diagnosis (train vs. validation/test comparison).
- An explicit statement that the leakage check (Module 4/5 rule) was performed on the final feature set.
- Any function under `src/` has at least a one-line docstring.
