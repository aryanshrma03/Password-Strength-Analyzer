from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
WORDLIST_PATH = DATA_DIR / "wordlists" / "common_passwords.txt"
