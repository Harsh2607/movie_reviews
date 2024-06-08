import requests
from .models import Movie, Genre

def fetch_movies_from_tmdb(api_key):
    url = 'https://api.themoviedb.org/3/movie/popular'
    params = {
        'api_key': api_key,
        'language': 'en-US',
        'page': 1
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    movies_data = response.json().get('results', [])

    for movie_data in movies_data:
        movie, created = Movie.objects.get_or_create(
            title=movie_data['title'],
            defaults={
                'description': movie_data['overview'],
                'release_date': movie_data['release_date'],
                'poster_url': f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
            }
        )
        for genre_data in movie_data.get('genre_ids', []):
            genre, _ = Genre.objects.get_or_create(id=genre_data)
            movie.genres.add(genre)

    return movies_data
