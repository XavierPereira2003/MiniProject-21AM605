from django.db import models
from django.contrib.auth.models import User
from cast.models import Cast
from movies.models import Movies
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

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


    def __str__(self) -> str:
        return self.user.username

# The following two funtions are the part's t
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Users.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    try:
        users_instance = Users.objects.get(user=instance)
    except Users.DoesNotExist:
        # If no Users instance exists for this User, skip saving
        return

    users_instance.bio = instance.users.bio
    users_instance.location = instance.users.location
    users_instance.birth_date = instance.users.birth_date
    users_instance.save()

    
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

    def __str__(self)->str:
        return slugify(f"{self.user.user.username}-{self.movie.title}")

