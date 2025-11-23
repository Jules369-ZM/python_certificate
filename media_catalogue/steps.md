# Media Catalogue Workshop Steps

## Step 1
Create a Movie class with __init__ taking self, title, year, director, duration, and assign them to attributes.

## Step 2
Add __str__ method to Movie that returns "title (year) - duration min, director".

## Step 3
Create movie1 instance of Movie and print it.

## Step 4-7
Add validations in Movie __init__: title strip == "", year < 1895, director strip == "", duration <= 0, raise ValueError.

## Step 8-12
Wrap movie1 creation in try-except for ValueError, print error if any.

## Step 13
Create TVSeries class inheriting from Movie, create instance series1, print it (inherits __str__).

## Step 14-15
Create MediaCatalogue with items = [], add method to append.

## Step 16-18
Add __init__ to MediaCatalogue, explain super.

## Step 19
Add __str__ to MediaCatalogue for empty case.

## Step 20-21
Add import and print docstrings.

## Step 22
Add __str__ override to MediaCatalogue with result = header, then return result (initially, then expand).

(Note: Steps 1-42 build incrementally, adding validations, docstrings, custom exceptions, inheritance, methods for filtering, and categorized display.)

The final system includes:
- Movie class with validations and display.
- TVSeries inheriting, adding seasons/total_episodes with validations and custom __str__.
- MediaError custom exception.
- MediaCatalogue with add, get_movies, get_tv_series, __str__ with separate sections for movies and series.
