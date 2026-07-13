clean_movies = []

for movie in rows:
    clean = {
        "title": movie["title"],
        "genres": extract_names(movie["genres"]),
        # add the remaining columns here...
        # production_companies also needs extract_names()
        # the rest are plain values like movie["budget"]
    }
    clean_movies.append(clean)

# verify
for m in clean_movies[:3]:
    print(m)