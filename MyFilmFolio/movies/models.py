from django.db import models
from django.db import models, Model


MOVIE_GENRES = [
    ("action", "Action"),
    ("adventure", "Adventure"),
    ("comedy", "Comedy"),
    ("drama", "Drama"),
    ("horror", "Horror"),
    ("science_fiction", "Science Fiction"),
    ("fantasy", "Fantasy"),
    ("romance", "Romance"),
    ("thriller", "Thriller"),
    ("documentary", "Documentary"),
    ("crime", "Crime"),
    ("mystery", "Mystery"),
    ("animation", "Animation"),
    ("family", "Family"),
    ("biography", "Biography"),
    ("history", "History"),
    ("war", "War"),
    ("musical", "Musical"),
    ("western", "Western"),
    ("film_noir", "Film Noir"),
]
# Create your models here.

class Movies(Model):
    """
    A class representing a movie in the database.
    """
    movie_id=models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=255)
    genre=models.CharField(max_length=255, choices=MOVIE_GENRES)   
    discription=models.TextField()
    release_date=models.DateField()
    poster_path=models.ImageField()

    def __str__(self):
        return "_".join(self.title.split())+str(self.movie_id)
    
    
