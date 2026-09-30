# Olist Delivery Risk Prediction

A classroom project: join and clean the Olist Brazilian E-Commerce dataset, then build a model that predicts whether an order will arrive late. You'll work through data preparation, exploration, a baseline and a real classifier, evaluation, and (optionally) a customer-segmentation extension.

This project applies the Data Science & Analytics track's curriculum (see `curriculum/`) to one real, messy dataset end to end.

## Modules

Each module below translates the curriculum's module text into this project's specific scope, objectives, and definition of done. The curriculum sets the skills; each module file sets what doing those skills looks like on this dataset.

| Module | File | Covers |
| --- | --- | --- |
| 4 — Data Preparation and Exploration | [modules/module-4-data-preparation.md](modules/module-4-data-preparation.md) | Loading, joining, cleaning, and exploring the raw tables |
| 5 — Supervised Learning | [modules/module-5-supervised-learning.md](modules/module-5-supervised-learning.md) | Baseline and classifier for the late-delivery prediction |
| 6 — Model Evaluation and Improvement | [modules/module-6-model-evaluation.md](modules/module-6-model-evaluation.md) | Evaluating the classifier with a metric appropriate to the imbalance |
| 7 — Unsupervised Learning (optional) | [modules/module-7-unsupervised-learning.md](modules/module-7-unsupervised-learning.md) | Bonus: RFM-style customer segmentation |

Work through them in order. Module 7 is optional and not required to complete the project.

## Data

The raw CSVs are not committed to this repo. See [data/README.md](data/README.md) for where to get them and where to put them.

## Setup

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
```

## Git workflow

1. **Fork this repository** to your own GitHub account.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/<your-github-username>/olist-delivery-risk-prediction.git
   cd olist-delivery-risk-prediction
   ```
3. **Create a branch** named after your GitHub username:
   ```bash
   git checkout -b submission/<your-github-username>
   ```
4. **Do all of your work inside your own folder**: `student-work/<your-github-username>/`. Don't edit files outside this folder — that's where notebooks, `src/` code, and your `docs/decision-log.md` should live.
5. **Commit and push your branch** to your fork:
   ```bash
   git push origin submission/<your-github-username>
   ```
6. **Open a pull request** from your fork's `submission/<your-github-username>` branch into this repository's `main` branch.

Your PR is your submission. Keep it scoped to your `student-work/<your-github-username>/` folder.

## Repository layout

```
README.md
curriculum/                      # original course curriculum (reference, don't edit)
modules/                         # this project's module-by-module scope and definition of done
data/                            # raw CSVs go here locally (not committed — see data/README.md)
student-work/<your-github-username>/   # your work goes here
```

The `notebooks/`, `src/`, and `requirements.txt` at the repo root are a small worked example showing how the raw tables get loaded — a reference, not something you need to build on directly. Your own version of that structure belongs inside your `student-work/<your-github-username>/` folder.
