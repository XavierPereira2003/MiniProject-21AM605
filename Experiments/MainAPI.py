from tmdbv3api import TMDb, Movie
from SecretsToo import api

class TMDbClient:
    def __init__(self, api_key):
        self.tmdb = TMDb()
        self.tmdb.api_key = api_key
        self.movie = Movie()

    def get_movie_details(self, movie_id):
        movie_details = self.movie.details(movie_id)
        movie_info = {
            'id': movie_details.id,
            'title': movie_details.title,
            'poster': movie_details.poster_path,
            'language': movie_details.original_language
        }
        return movie_info

    def get_movie_actors(self, movie_id):
        actors = self.movie.credits(movie_id)['cast']
        actors_info = [{'name': actor['name'], 'image': actor['profile_path']} for actor in actors[:5]]
        return actors_info

    def get_movie_directors(self, movie_id):
        directors = [crew_member for crew_member in self.movie.credits(movie_id)['crew'] if crew_member['job'] == 'Director']
        directors_info = [{'name': director['name'], 'image': director['profile_path']} for director in directors]
        return directors_info

# Example usage:
if __name__ == "__main__":
    tmdb_client = TMDbClient(api_key=api)

    # Get details of a specific movie
    movie_id = 603  # Example movie ID
    movie_details = tmdb_client.get_movie_details(movie_id)
    print("Movie details:")
    print("ID:", movie_details['id'])
    print("Title:", movie_details['title'])
    print("Poster:", movie_details['poster'])
    print("Language:", movie_details['language'])

    # Get actors of the movie
    actors = tmdb_client.get_movie_actors(movie_id)
    print("\nActors:")
    for actor in actors:
        print("- Name:", actor['name'])
        print("  Image:", actor['image'])

    # Get directors of the movie
    directors = tmdb_client.get_movie_directors(movie_id)
    print("\nDirectors:")
    for director in directors:
        print("- Name:", director['name'])
        print("  Image:", director['image'])
