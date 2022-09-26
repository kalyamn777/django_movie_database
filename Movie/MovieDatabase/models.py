from django.db import models

# Create your models here.

class MovieNames(models.Model):
    movie_name = models.CharField(max_length=50)
    actor_name=models.CharField(max_length=30)
    actress_name=models.CharField(max_length=30)
    release_year=models.IntegerField()
    director_name=models.CharField(max_length=30)

    def __str__(self):
        return self.movie_name


