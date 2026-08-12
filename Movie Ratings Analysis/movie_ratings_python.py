import csv

def calculate_rating_stats(data, industry = None):
    """
    Calculate minimum, maximum, and average IMDb rating.

    If an industry is provided, statistics are calculated
    only for movies belonging to that industry.
    """

    # Store valid IMDb ratings for the selected movies
    ratings = []

    # Process each movie record
    for row in data:

        # Check that IMDb rating is not NULL.
        # If industry is provided, also filter by that industry.
        if row[4]!='NULL' and (not industry or row[2]==industry):
            ratings.append(float(row[4]))

    # Calculate rating statistics        
    min_rating = min(ratings)
    max_rating = max(ratings)
    avg_rating = sum(ratings)/len(ratings)
    
    return min_rating, max_rating, avg_rating

# Read movie data from the CSV file
with open("movies.csv") as f:
    data = list(csv.reader(f))

# Separate the header row from the movie records    
header = data[0]
data = data[1:]

# Calculate statistics for all movies
min_rating, max_rating, avg_rating = calculate_rating_stats(data)
print(f"All records : Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")

# Calculate statistics for Bollywood movies
min_rating, max_rating, avg_rating = calculate_rating_stats(data, industry = 'Bollywood')
print(f"Bollywood   : Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")

# Calculate statistics for Hollywood movies
min_rating, max_rating, avg_rating = calculate_rating_stats(data, industry = 'Hollywood')
print(f"Hollywood   : Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")