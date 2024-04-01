
from django.db import models
from django.db.models import Model
from django.utils.text import slugify
# Create your models here.

class Cast(Model):
    """
    Represents a cast member in the database.   
    """
    cast_id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=255)
    DoB=models.DateField()
    Image=models.ImageField()

    def __str__(self):
        return f"{slugify(self.name)}-{str(self.cast_id)}"
