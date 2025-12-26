from django.db import models

class Hero(models.Model):
    hero_name = models.CharField(max_length=100)
    age = models.IntegerField()
    movies = models.CharField(max_length=200)
    dob = models.DateField()
    no_of_movies = models.IntegerField()

    def __str__(self):
        return self.hero_name


# Create your models here.
