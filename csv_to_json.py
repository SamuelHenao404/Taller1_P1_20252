import pandas as pd
import json

df = pd.read_csv('IMDBMovies.csv')

df.to_json('IMDbMovies.json', orient='records')

with open('IMDbMovies.json', 'r') as file:
    movies = json.load(file)

for i in range(100):
    movie = movies[i]
    print(movie)
    break
