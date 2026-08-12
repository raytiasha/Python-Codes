import pandas as pd

# Load the movie dataset
df = pd.read_csv("movies.csv")

# Analyze all movies
print(f"All records: Min rating = {df['imdb_rating'].min()}, Max rating = {df['imdb_rating'].max()}, Mean rating = {df['imdb_rating'].mean()}")

# Analyze Bollywood movies
df_bollywood = df[df.industry == "Bollywood"]
print(f"Bollywood movies: Min rating = {df_bollywood['imdb_rating'].min()}, Max rating = {df_bollywood['imdb_rating'].max()}, Mean rating = {df_bollywood['imdb_rating'].mean()}")

# Analyze Hollywood movies
df_hollywood = df[df.industry == "Hollywood"]
print(f"Hollywood movies: Min rating = {df_hollywood['imdb_rating'].min()}, Max rating = {df_hollywood['imdb_rating'].max()}, Mean rating = {df_hollywood['imdb_rating'].mean()}")