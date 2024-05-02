from django.db import models
from django.db.models import Model
from django.utils.text import slugify
from cast.models import Cast
from django.core.files.storage import FileSystemStorage
moviesPics= FileSystemStorage(location="movie_images")

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

class Genre(Model):
    genre=models.CharField(max_length=255, choices=MOVIE_GENRES)
class Movies(Model):
    """
    A class representing a movie in the database.
    """
    movie_id=models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=255)
    genre=models.ManyToManyField(Genre,related_name="movies")
    director=models.ForeignKey(Cast, on_delete=models.DO_NOTHING)
    discription=models.TextField()
    release_date=models.DateField()
    poster_path=models.ImageField(storage=moviesPics)
    slug=models.SlugField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.title)}-{str(self.movie_id)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{slugify(self.title)}-{str(self.movie_id)}"
    
    
class Roles(Model):
    """
    A class representing a role played by a cast member in a movie.
    """
    role_id=models.BigAutoField(primary_key=True)
    movie=models.ForeignKey(Movies, on_delete=models.DO_NOTHING)
    cast=models.ForeignKey(Cast, on_delete=models.DO_NOTHING)
    role_name=models.CharField(max_length=255)

    