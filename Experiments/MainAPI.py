import os
from tmdbv3api import TMDb, Movie, Person
from dotenv import load_dotenv, dotenv_values


load_dotenv()

class TMDbClient:
    def __init__(self, api_key):
        self.tmdb = TMDb()
        self.tmdb.api_key = api_key
        self.movie = Movie()
        self.person = Person()

    def get_movie_details(self, movie_id):
        movie_details = self.movie.details(movie_id)
        credits = self.movie.credits(movie_id)
        director = None
        director_id = None
        director_image = None
        actors = []
        actor_ids = []  # Store actor IDs separately
        actor_images = {}  # Store actor images
        for crew_member in credits['crew']:
            if crew_member['job'] == 'Director':
                director = crew_member['name']
                director_id = crew_member['id']  # Store director's ID
                director_details = self.person.details(director_id)
                director_image = director_details.profile_path  # Retrieve director's image URL

        count = 0  # To Limit The number of Actors fetched, using this since [:5] was not working
        for actor in credits['cast']:
            if count > 5:
                break
            actors.append(actor['name'])
            actor_ids.append(actor['id'])  # Store actor IDs
            actor_details = self.person.details(actor['id'])
            actor_images[actor['id']] = actor_details.profile_path  # Retrieve actor's image URL
            count += 1
        movie_info = {
            'id': movie_details.id,
            'title': movie_details.title,
            'poster': movie_details.poster_path,
            'language': movie_details.original_language,
            'director': director,
            'director_id': director_id,  # Include director's ID
            'director_image': director_image,  # Include director's image URL
            'actors': actors,
            'actor_ids': actor_ids,  # Include actor IDs in the returned dictionary
            'actor_images': actor_images  # Include actor images dictionary
        }
        return movie_info


# Example usage:
if __name__ == "__main__":
    tmdb_client = TMDbClient(api_key=os.getenv('api'))

    # Get details of a specific movie
    movie_id = 603  # Example movie ID
    movie_details = tmdb_client.get_movie_details(movie_id)
    print("Movie details:")
    print("ID:", movie_details['id'])
    print("Title:", movie_details['title'])
    print("Poster:", movie_details['poster'])
    print("Language:", movie_details['language'])
    print("Director:", movie_details['director'])
    print("Director ID:", movie_details['director_id'])
    print("Director Image:", movie_details['director_image'])
    print("Actors:", ", ".join(movie_details['actors']))
    # print("Actor IDs:", ", ".join(str(actor_id) for actor_id in movie_details['actor_ids']))
    for actor_id, actor_image in movie_details['actor_images'].items():
        print(f"Actor ID: {actor_id}, Actor Image: {actor_image}")
