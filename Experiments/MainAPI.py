from tmdbv3api import TMDb, Movie, Discover
from SecretsToo import api

class TMDbClient:
    def __init__(self, api_key):
        self.tmdb = TMDb()
        self.tmdb.api_key = api_key
        self.movie = Movie()
        self.discover = Discover()

    def search_movie(self, query):
        return self.movie.search(query)

    def get_movie_details(self, movie_id):
        return self.movie.details(movie_id)

    def get_popular_movies(self):
        return self.movie.popular()

    def get_movie_recommendations(self, m_id):
        return self.movie.recommendations(movie_id=m_id)

# Example usage:
if __name__ == "__main__":
    tmdb_client = TMDbClient(api_key=api)

    # Search for a movie
    search_results = tmdb_client.search_movie("The Matrix")
    print("Search results:")
    for result in search_results:
        print(result.title)

    # Get details of a specific movie
    movie_id = 603
    movie_details = tmdb_client.get_movie_details(movie_id)
    print("\nMovie details:")
    print(movie_details.title)
    print(movie_details.overview)

    # Get popular movies
    popular_movies = tmdb_client.get_popular_movies()
    print("\nPopular movies:")
    for movie in popular_movies:
        print(movie.title)

    # Get movie recommendations
    movie_id = 603
    recommendations = tmdb_client.get_movie_recommendations(movie_id)
    print("\nRecommendations for The Matrix:")
    for recommendation in recommendations:
        print(recommendation.title)
