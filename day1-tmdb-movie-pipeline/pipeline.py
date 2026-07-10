import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "tmdb_5000_movies.csv"

with DATA_PATH.open("r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
print(f"Loaded {len(rows)} movies from {DATA_PATH}")

for row in rows[:5]:
    genres = json.loads(row['genres'])
    print(f"{row['title']} -> {genres}")
