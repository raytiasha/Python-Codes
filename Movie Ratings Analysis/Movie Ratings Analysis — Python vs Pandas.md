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
View the code [here]().
