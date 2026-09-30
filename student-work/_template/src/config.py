"""Project paths."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = PROJECT_ROOT.parent.parent
RAW_DATA_DIR = REPO_ROOT / "data"
