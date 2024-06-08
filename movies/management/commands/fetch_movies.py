import requests
from django.core.management.base import BaseCommand
from movies.models import Genre, Movie
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetch movies from TMDb and store in database'

    def handle(self, *args, **kwargs):
        api_key = '2123ae880ddb82d7f86b90eef77fe95f'
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'
        response = requests.get(url)
        movies = response.json().get('results', [])

        for movie_data in movies:
            movie, created = Movie.objects.get_or_create(
                title=movie_data['title'],
                description=movie_data['overview'],
                release_date=datetime.strptime(movie_data['release_date'], '%Y-%m-%d').date(),
                poster_url=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}",
            )

            for genre_id in movie_data['genre_ids']:
                genre, _ = Genre.objects.get_or_create(id=genre_id)
                movie.genres.add(genre)
            
        self.stdout.write(self.style.SUCCESS('Successfully fetched and stored movies'))
