from django.urls import path
from .views import MovieRecommendationView

urlpatterns = [
    path('', MovieRecommendationView.as_view(), name='movie-recommendations'),
]
