import sys
import json
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from cast.models import Cast
from movies.models import Genre, Movies, Roles


class Command(BaseCommand):
    help = 'Insert data from tmdbsave.json file into the database'

    def handle(self, *args, **options):
        # Read data from tmdbsave.json file
        with open('../Experiments/tmdbsave9.json', 'r') as file:
            tmdb_data = json.load(file)

        # Insert genres
        for movie_data in tmdb_data['movie_details']:
            genres = [Genre.objects.get_or_create(genre=genre_name)[0] for genre_name in movie_data['genre']]
            movie_data['genre'] = genres

        # Insert cast
        for cast_data in tmdb_data['persons']:
            cast_id = cast_data['id']
            name = cast_data['name']
            dob = cast_data.get('birth_date')
            image = cast_data.get('image')
            bio = cast_data.get('biography')
            slug = slugify(name) + "-" + str(cast_id)  # Generate slug using name and cast_id

            # Check if cast with cast_id already exists
            cast, created = Cast.objects.get_or_create(
                cast_id=cast_id,
                defaults={
                    'name': name,
                    'DoB': dob,
                    'Image': image,
                    'bio': bio,
                    'slug': slug  # Set the slug field
                }
            )

            # if cast is newly created then proceed
            if created:
                cast.slug = slug
                cast.save()

        # Insert movies
        for movie_data in tmdb_data['movie_details']:
            movie_id = movie_data['movie_id']
            title = movie_data['title']
            description = movie_data['description']
            release_date = movie_data['release_date']
            poster = movie_data['poster']
            director_id = movie_data['director']
            vote_average = movie_data['vote_average']
            director = Cast.objects.get(cast_id=director_id)

            movie, created = Movies.objects.get_or_create(
                movie_id=movie_id,
                defaults={
                    'title': title,
                    'description': description,
                    'release_date': release_date,
                    'poster_path': poster,
                    'director': director,
                    'vote_average': vote_average,
                    'slug': slugify(title) + "-" + str(movie_id)
                }
            )

            # If the movie is newly created, set its genre and write its avg. vote
            if created:
                genres = [Genre.objects.get_or_create(genre=genre_name)[0] for genre_name in movie_data['genre']]
                movie.genre.set(genres)  # Set many-to-many relationship

                movie.save()

        # Insert roles
        for roles_data in tmdb_data['roles']:
            for movie_id, roles in roles_data.items():
                # Retrieve the movie instance
                movie = Movies.objects.get(movie_id=movie_id)

                # Iterate over roles for the current movie
                for cast_id, role_name in roles.items():
                    # Retrieve the cast member instance
                    cast = Cast.objects.get(cast_id=cast_id)

                    # Create or get the role instance
                    role, created = Roles.objects.get_or_create(
                        movie=movie,
                        cast=cast,
                        role_name=role_name
                    )

                    # If the role was not created (i.e., it already exists), update the role name
                    if not created:
                        role.role_name = role_name
                        role.save()


def main():
    command = Command()
    command.execute()


if __name__ == "__main__":
    main()
