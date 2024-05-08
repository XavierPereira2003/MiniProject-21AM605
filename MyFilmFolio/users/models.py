from django.db import models
from django.contrib.auth.models import User
from cast.models import Cast
from movies.models import Movies
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Users(models.Model):
    """
    Extedin the user model in django,

    Args:
        models (_type_): _description_
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class favCast(models.Model):
    """
    Class Indicating the users Favorite Cast Member

    Args:
        models (_type_): _description_
    """
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    cast = models.ForeignKey(Cast, on_delete=models.CASCADE)

class movieReview(models.Model):
    """
    Class Indicating the users Favorite Cast Member

    Args:
        models (_type_): _description_
    """
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    review=models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)],blank=True)

