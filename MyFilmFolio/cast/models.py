
from django.db import models
from django.db.models import Model
# Create your models here.

class cast(Model):
    cast_id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=255)
    DoB=models.DateField()
    Image=models.ImageField()
    
    def __str__(self):
        return self.name
