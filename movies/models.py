from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255)
    movies = models.ManyToManyField('Movie', related_name='genres_set')
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre, related_name='movies_set_in_movies')  # Updated related_name
    poster_url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title

