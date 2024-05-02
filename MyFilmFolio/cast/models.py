
from django.db import models
from django.db.models import Model
from django.utils.text import slugify
from django.core.files.storage import FileSystemStorage

castPics= FileSystemStorage(location="cast_images")
# Create your models here.

class Cast(Model):
    """
    Represents a cast member in the database.   
    """
    cast_id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=255)
    DoB=models.DateField()
    Image=models.ImageField(storage=castPics)
    slug=models.SlugField(max_length=255, unique=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.name)}-{str(self.cast_id)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{slugify(self.name)}-{str(self.cast_id)}"
