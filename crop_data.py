import pandas as pd

df = pd.read_csv("./rating.csv", sep=",")
print("Users:", len(df["userId"].unique()))
print("Movies:", len(df["movieId"].unique()))
user_counts = df["userId"].value_counts()
top_users = user_counts[user_counts > user_counts.quantile(0.97)]
df = df[df["userId"].isin(top_users.index)]

movie_counts = df["movieId"].value_counts()
top_movies = movie_counts[movie_counts > movie_counts.quantile(0.97)]
df = df[df["movieId"].isin(top_movies.index)]
print(df.shape)
print("Users:", len(df["userId"].unique()))
print("Movies:", len(df["movieId"].unique()))

df.to_csv("rating_filtered.csv", sep=";")
