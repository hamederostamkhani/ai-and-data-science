import pandas as pd

class MovieRecommender:
    def __init__(self, data_path="../data"):
        
        ratings = pd.read_csv(f"{data_path}/ratings.csv")
        movies = pd.read_csv(f"{data_path}/movies.csv")

        self.movie_list = movies["title"].to_list()

        self.data = pd.merge(ratings, movies, on="movieId")

        self.movie_matrix = self.data.pivot_table(
            index="userId",
            columns="title",
            values="rating"
        )

        ratings_count = self.data.groupby("title")["rating"].count()
        ratings_mean = self.data.groupby("title")["rating"].mean()

        self.movie_stats = pd.DataFrame({
            "rating_count": ratings_count,
            "rating_mean": ratings_mean
        })

    def recommend(self, movie_name, min_ratings=50):

        movie_ratings = self.movie_matrix[movie_name]

        similar_movies = self.movie_matrix.corrwith(movie_ratings)

        corr_df = pd.DataFrame(similar_movies, columns=["correlation"])
        corr_df.dropna(inplace=True)

        corr_df = corr_df.join(self.movie_stats["rating_count"])

        recommendations = corr_df[
            corr_df["rating_count"] > min_ratings
        ].sort_values("correlation", ascending=False)

        return recommendations.head(10)
