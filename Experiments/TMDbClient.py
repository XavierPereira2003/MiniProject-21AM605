import os
import json
from tmdbv3api import TMDb, Movie, Person, Discover
from dotenv import load_dotenv, dotenv_values
from PopulateDB import DatabaseManager

load_dotenv()

genre_mapping = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    99: "Documentary",
    18: "Drama",
    10751: "Family",
    14: "Fantasy",
    36: "History",
    27: "Horror",
    10402: "Music",
    9648: "Mystery",
    10749: "Romance",
    878: "Science Fiction",
    10770: "TV Movie",
    53: "Thriller",
    10752: "War",
    37: "Western"
}


class TMDbClient:
    def __init__(self, api_key):
        self.tmdb = TMDb()
        self.tmdb.api_key = api_key
        self.movie = Movie()
        self.person = Person()
        self.discover = Discover()

    def get_info(self, count=2, year='2024', save_to_file = False, file_name = "tmdbsave.json"):
        '''
        Gets English Movies, Persons, Actor Roles and Directors information
        :param count: number of movies to return default 2 pages (i.e. 20 Movies)
        :param year: year of movies to return
        '''
        try:
            movie_details = []
            persons = []
            roles = []
            directs = []
            for page in range(1, count):
                popular_list = self.discover.discover_movies(
                    {'with_original_language': 'en', 'year': year, 'sort_by': 'popularity.desc', 'page': page}).results

                for sublist in popular_list:
                    id = sublist['id']

                    credits = self.movie.credits(id)
                    director_info = self.__extract_director_info(credits)
                    actors_info, actors_role = self.__extract_actors_info(credits)

                    language = sublist['original_language']
                    title = sublist['title']
                    genre = [genre_mapping[id] for id in sublist['genre_ids']]
                    overview = sublist['overview']
                    poster = sublist['poster_path']
                    release_date = sublist['release_date']
                    vote_average = sublist['vote_average']
                    director = director_info['id']

                    directs.append({'id': director_info['id'], 'movie': sublist['id']})
                    persons.append(director_info)

                    roles.append({id: actors_role})
                    for actor in actors_info:
                        persons.append(actor)

                    movie = {'movie_id': id, 'language': language, 'title': title, 'genre': genre,
                             'description': overview, 'poster': poster, 'director':director, 'release_date': release_date,
                             'vote_average': vote_average}
                    movie_details.append(movie)

            if save_to_file:
                with open(file_name, 'w') as f:
                    json.dump({'movie_details': movie_details, 'persons': persons, 'roles': roles, 'directs': directs},
                              f, indent=4)

            return {'movie_details': movie_details, 'persons': persons, 'roles': roles, 'directs': directs}

        except Exception as e:
            print(e)
            return {}

    def __extract_director_info(self, credits):
        director_info = {}
        for crew_member in credits['crew']:
            if crew_member['job'] == 'Director':
                director_info['id'] = crew_member['id']
                director_info['name'] = crew_member['name']
                director_details = self.person.details(director_info['id'])
                director_info['image'] = director_details.profile_path
                director_info['birth_date'] = director_details.birthday
                director_info['biography'] = director_details.biography
                break  # Assuming only one director for simplicity
        return director_info

    def __extract_actors_info(self, credits):
        actors_info = []
        actors_role = {}
        count = 0
        for actor in credits['cast']:
            if count > 5:
                break
            actor_info = {}
            actor_info['id'] = actor['id']
            actor_info['name'] = actor['name']
            actors_role.update({actor['id']:actor['character']})
            actor_details = self.person.details(actor_info['id'])
            actor_info['image'] = actor_details.profile_path
            actor_info['birth_date'] = actor_details.birthday
            actor_info['biography'] = actor_details.biography
            actors_info.append(actor_info)
            count += 1
        return actors_info, actors_role



# Example usage:
tmdb_client = TMDbClient(api_key=os.getenv('api'))
info = tmdb_client.get_info(save_to_file=True, year='2023')

print(info)

# # Example usage:
# db_manager = DatabaseManager(
#     dbname='your_database_name',
#     user='your_username',
#     password='your_password',
#     host='your_host',
#     port='your_port'
# )
# db_manager.populate_database(movie_detials, persons, roles, directs)