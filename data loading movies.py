# ===========================================
# Leonardo DiCaprio Movie Analytics
# ===========================================

import pandas as pd
import matplotlib.pyplot as plt
import ast

# -------------------------------
# Chart Theme
# -------------------------------
plt.style.use("ggplot")

REVENUE_COLOR = "#DAA520"     # Gold
RATING_COLOR = "#4169E1"      # Royal Blue
PROFIT_COLOR = "#228B22"      # Forest Green
DIRECTOR_COLOR = "#800080"    # Purple
EDGE_COLOR = "black"

TITLE_SIZE = 16
LABEL_SIZE = 12

# -------------------------------
# Load Dataset
# -------------------------------

movies = pd.read_csv(r"C:\Users\hrish\OneDrive\Desktop\filmography analysis project\movies dataset\tmdb_5000_movies.csv")

credits = pd.read_csv(r"C:\Users\hrish\OneDrive\Desktop\filmography analysis project\movies dataset\tmdb_5000_credits.csv")

# -------------------------------
# Merge Dataset
# -------------------------------

df = movies.merge(credits, on="title")

print(df.head())
print(df.shape)

# -------------------------------
# Filter Leonardo Movies
# -------------------------------

leo = df[df["cast"].str.contains("Leonardo DiCaprio", case=False, na=False)].copy()

print("Total Leonardo Movies:", len(leo))

# -------------------------------
# Extract Genres
# -------------------------------

def get_genres(text):
    genres = ast.literal_eval(text)
    return ", ".join([g["name"] for g in genres])

# -------------------------------
# Extract Director
# -------------------------------

def get_director(text):
    crew = ast.literal_eval(text)

    for member in crew:
        if member["job"] == "Director":
            return member["name"]

    return None

leo["genres"] = leo["genres"].apply(get_genres)
leo["director"] = leo["crew"].apply(get_director)

# -------------------------------
# Date & Profit
# -------------------------------

leo["release_date"] = pd.to_datetime(leo["release_date"])

leo["release_year"] = leo["release_date"].dt.year

leo["profit"] = leo["revenue"] - leo["budget"]

# -------------------------------
# Save Final Dataset
# -------------------------------

leo.to_csv("leonardo_movies_final.csv", index=False)

print("Dataset Saved Successfully!")

# ===================================================
# EDA
# ===================================================

print(leo.describe())

print(leo.isnull().sum())

# ===================================================
# Top Revenue Movies
# ===================================================

top_revenue = leo.sort_values("revenue", ascending=False).head(10)

plt.figure(figsize=(12,6))

plt.bar(
    top_revenue["title"],
    top_revenue["revenue"],
    color=REVENUE_COLOR,
    edgecolor=EDGE_COLOR
)

plt.title("Top 10 Highest Grossing Leonardo DiCaprio Movies", fontsize=TITLE_SIZE)

plt.xlabel("Movie", fontsize=LABEL_SIZE)

plt.ylabel("Revenue ($)", fontsize=LABEL_SIZE)

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()

# ===================================================
# Highest Rated Movies
# ===================================================

top_rating = leo.sort_values("vote_average", ascending=False).head(10)

plt.figure(figsize=(12,6))

plt.bar(
    top_rating["title"],
    top_rating["vote_average"],
    color=RATING_COLOR,
    edgecolor=EDGE_COLOR
)

plt.title("Top Rated Leonardo DiCaprio Movies", fontsize=TITLE_SIZE)

plt.xlabel("Movie", fontsize=LABEL_SIZE)

plt.ylabel("IMDb Rating", fontsize=LABEL_SIZE)

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()

# ===================================================
# Highest Profit Movies
# ===================================================

top_profit = leo.sort_values("profit", ascending=False).head(10)

plt.figure(figsize=(12,6))

plt.bar(
    top_profit["title"],
    top_profit["profit"],
    color=PROFIT_COLOR,
    edgecolor=EDGE_COLOR
)

plt.title("Most Profitable Leonardo DiCaprio Movies", fontsize=TITLE_SIZE)

plt.xlabel("Movie", fontsize=LABEL_SIZE)

plt.ylabel("Profit ($)", fontsize=LABEL_SIZE)

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()

# ===================================================
# Movies Released Over Time
# ===================================================

plt.figure(figsize=(10,5))

plt.plot(
    leo.sort_values("release_year")["release_year"],
    leo.sort_values("release_year")["vote_average"],
    marker="o",
    linewidth=2,
    color="darkblue"
)

plt.title("IMDb Rating Trend Over Time", fontsize=TITLE_SIZE)

plt.xlabel("Release Year")

plt.ylabel("IMDb Rating")

plt.tight_layout()

plt.show()

# ===================================================
# Budget vs Revenue
# ===================================================

plt.figure(figsize=(8,6))

plt.scatter(
    leo["budget"],
    leo["revenue"],
    color="darkorange",
    s=100
)

plt.title("Budget vs Revenue", fontsize=TITLE_SIZE)

plt.xlabel("Budget")

plt.ylabel("Revenue")

plt.tight_layout()

plt.show()

# ===================================================
# Director Collaborations
# ===================================================

director_count = leo["director"].value_counts()

plt.figure(figsize=(10,6))

director_count.plot(
    kind="bar",
    color=DIRECTOR_COLOR,
    edgecolor=EDGE_COLOR
)

plt.title("Leonardo DiCaprio Collaborations by Director", fontsize=TITLE_SIZE)

plt.xlabel("Director")

plt.ylabel("Number of Movies")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()

# ===================================================
# Runtime Distribution
# ===================================================

plt.figure(figsize=(8,5))

plt.hist(
    leo["runtime"],
    bins=10,
    color="teal",
    edgecolor="black"
)

plt.title("Movie Runtime Distribution", fontsize=TITLE_SIZE)

plt.xlabel("Runtime (Minutes)")

plt.ylabel("Frequency")

plt.tight_layout()

plt.show()

print("Analysis Completed Successfully!")