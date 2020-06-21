# Importing the libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Reading the csv
base = pd.read_csv("Movies.csv")

# Get some initial informations of the dataframe
base.head()
base.info()
base.describe()

# Counting the movies watched at the theather
base.loc[base.CINEMA == True, "CINEMA"].count()

# Ratings Distribution
rating_boxplot = sns.boxplot(y=base["RATING"], color="royalblue", medianprops={
                             "color": "red", "linestyle": "--"}).set_title("Ratings Distribution")

# Finding the outliers movies
def minimum_rating(csv):
    for index, row in csv.iterrows():
        if row["RATING"] == 1:
            print(row["MOVIE"], row["YEAR"])

minimum_rating(base)

# Movie Year Distribution
cont = base["YEAR"].value_counts()

bar = plt.bar(cont.index, cont.values, color="deepskyblue", width=0.5)
plt.gca().set(title="Release Movie Year Distribution", xlabel="Year", ylabel="Watched")
plt.grid(axis="y", color='black', linestyle='--', linewidth=0.3, alpha=0.7)
plt.xticks(rotation=45)
plt.xticks(np.arange(1940, 2025, 5))
plt.yticks(np.arange(0, 50, 10))

# Most  Watched Release Year Movie
year = base.groupby("YEAR")
year_cont = year.count()
cont = year_cont.nlargest(5, "MOVIE")
most_watched = year.get_group(2017)

# Function to print the name of all 2017-movies
for index, row in base.iterrows():
    if row["YEAR"] == 2017:
        print(row["MOVIE"])

# Distribution ratings for the 2017 movies
year_box = sns.boxplot(y=most_watched["RATING"], color="palegreen", medianprops={
                       "color": "darkblue", "linestyle": "--"}).set_title("Ratings of 2017 Movies")

# Maximum rating movies and distribution
def maximum_rating(csv):
    for index, row in csv.iterrows():
        if row["RATING"] == 5:
            print(row["MOVIE"], row["YEAR"])

ax = maximum_rating(base)

# Agregate the movies by the maximum rating
rating = base.groupby("RATING")
maximum_rating_movies = rating.get_group(5)

# Building the graph of release year distribution of the maximum rating movies
scatter = sns.scatterplot(x=maximum_rating_movies["YEAR"], y=maximum_rating_movies["MOVIE"],
                          data=maximum_rating_movies, color="slateblue", s=120, alpha=0.8)
scatter.set_title("Release Years Distribution of Maximum Rating Movies")
scatter.set(yticklabels=[])
scatter.axes.get_yaxis().set_visible(False)
scatter.set_xticks(range(1940, 2025, 5))
plt.xticks(rotation=45)
