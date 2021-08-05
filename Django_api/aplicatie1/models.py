# Create your models here.
from django.db import models
# Create your views here.


class Location(models.Model):

    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city} - {self.country}"
