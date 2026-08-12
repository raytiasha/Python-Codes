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
- Optionally filters movies by industry.
- Stores valid ratings in a list.
- Calculates minimum, maximum, and average ratings.
  
View the code [here](https://github.com/raytiasha/Python-Codes/blob/main/Movie%20Ratings%20Analysis/movie_ratings_python.py).

## Approach 2: Pandas

The second implementation uses Pandas DataFrames, which handles many of the manual data-processing steps required in the pure Python approach.

View the code [here](https://github.com/raytiasha/Python-Codes/blob/main/Movie%20Ratings%20Analysis/movie_ratings_pandas.py).

### The key difference

Pure Python focuses on how to process each record.
Pandas allows you to focus more directly on what you want to analyze.

### Related Technical Blog

Read the full technical blog on [LinkedIn](https://www.linkedin.com/pulse/movie-ratings-analysis-python-vs-pandas-tiasha-ray-0ptnc/).
