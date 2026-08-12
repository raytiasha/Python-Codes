# Movie Ratings Analysis — Python vs Pandas

The objective of this project is to demonstrate how Pandas make a data-analysis task shorter, cleaner, and easier to maintain compared with using Python's built-in csv module alone.

The goal is to calculate the minimum, maximum, and average IMDb rating for:

- All movies
- Bollywood movies
- Hollywood movies

## Approach 1: Pure Python

The first implementation uses Python's built-in csv module.

The program:

- Reads the CSV file.
- Separates the header from the data.
- Iterates through each movie record.
- Filters out missing IMDb ratings.
- Optionally filters movies by industry.
- Stores valid ratings in a list.
- Calculates minimum, maximum, and average ratings.
View the code [here](https://github.com/raytiasha/Python-Codes/blob/main/Movie%20Ratings%20Analysis/movie_ratings_python.py).

## Approach 2: Pandas

The second implementation uses Pandas DataFrames.

View the code [here](https://github.com/raytiasha/Python-Codes/blob/main/Movie%20Ratings%20Analysis/movie_ratings_pandas.py).

This removes much of the manual data-processing code required with the csv module.

### The key difference

Pure Python focuses on how to process each record.
Pandas allows you to focus more directly on what you want to analyze.

### Related Technical Blog

This project is accompanied by a technical blog explaining the transition from pure Python to Pandas and the key data-analysis concepts learned along the way.
