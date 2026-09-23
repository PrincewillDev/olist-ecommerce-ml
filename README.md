# Olist E-Commerce ML

Exploration and modeling on the Brazilian E-Commerce Public Dataset by Olist.

## Setup

```powershell
python -m venv venv
./venv/Scripts/Activate.ps1
pip install -r requirements.txt
```

## Structure

```
datasets/
  raw_data/          # raw Olist CSVs (gitignored, not tracked in git)
notebooks/
  01_load_raw_data.ipynb   # loads each raw table individually, no joins yet
src/
  config.py          # project paths
  data_loader.py      # one loader function per raw CSV
requirements.txt
```

## Data

Source: [Olist Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle). Place the CSVs in `datasets/raw_data/` if they aren't already there.
