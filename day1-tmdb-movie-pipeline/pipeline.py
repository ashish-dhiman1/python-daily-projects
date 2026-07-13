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
    try:
        parsed = json.loads(json_string)
        genres_names=[]
        for item in parsed:
            genres_names.append(item['name'])
        return "|".join(genres_names)
    except (json.JSONDecodeError, TypeError):
        return ""

                                                       

clean_movies=[]
bad_data_count = 0                                    

for movie in rows:
    genres = extract_names(movie['genres'])             
    companies = extract_names(movie['production_companies'])  

    if genres == "" or companies == "":                 
        bad_data_count += 1                           

    clean_data = {
        'title':movie['title'],
        'genres': genres,                              
        'original_language':movie['original_language'],
        'budget':movie['budget'],
        'revenue':movie['revenue'],
        'runtime' : movie['runtime'],
        'vote_average':movie['vote_average'],
        'vote_count':movie['vote_count'],
        'release_date':movie['release_date'],
        'production_companies': companies             
    }
    clean_movies.append(clean_data)

for movie in clean_movies[:3]:
    print(movie)

print(f"Processed {len(rows)} movies, {bad_data_count} had missing/bad data") 