from django.db import models
from django.contrib.auth import get_user_model
from movies.models import Movie

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_by_user')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews_by_movie')
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.movie.title}"

