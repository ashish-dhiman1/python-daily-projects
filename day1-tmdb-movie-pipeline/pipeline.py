import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "tmdb_5000_movies.csv"

with DATA_PATH.open("r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
print(f"Loaded {len(rows)} movies from {DATA_PATH}")


def extract_names(json_string):
    parsed = json.loads(json_string)
    genres_names=[]
    for item in parsed:
        genres_names.append(item['name'])
    return "|".join(genres_names)

for movie in rows[:30]:
    genres_names = extract_names(movie['genres'])
    #print(f"{movie['title']} | {genres_names}")


clean_movies=[]

for movie in rows:
    clean_data = {
        'title':movie['title'],
        'genres':extract_names(movie['genres']),
        'original_language':movie['original_language'],
        'budget':movie['budget'],
        'revenue':movie['revenue'], 
        'runtime' : movie['runtime'], 
        'vote_average':movie['vote_average'], 
        'vote_count':movie['vote_count'], 
        'release_date':movie['release_date'],
        'production_companies' : extract_names(movie['production_companies'])
    }
    clean_movies.append(clean_data)

for movie in clean_movies[:3]:
    print(movie)
