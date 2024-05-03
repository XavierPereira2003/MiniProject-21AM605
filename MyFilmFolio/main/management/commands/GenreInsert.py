from django.core.management.base import BaseCommand
from movies.models import Genre

class Command(BaseCommand):
    help = 'Inserts predefined genres into the database'

    def handle(self, *args, **options):
        # Your genre insertion code here
        GENRES = [
            "Action",
            "Adventure",
            "Comedy",
            "Drama",
            "Horror",
            "Science Fiction",
            "Fantasy",
            "Romance",
            "Thriller",
            "Documentary",
            "Crime",
            "Mystery",
            "Animation",
            "Family",
            "Biography",
            "History",
            "War",
            "Musical",
            "Western",
            "Film Noir",
        ]

        for genre_name in GENRES:
            Genre.objects.get_or_create(genre=genre_name)

        self.stdout.write(self.style.SUCCESS('Genres inserted successfully'))

