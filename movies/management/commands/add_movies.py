from django.core.management.base import BaseCommand
from movies.models import Genre, Movie
from datetime import date

class Command(BaseCommand):
    help = 'Add initial movie data to the database'

    def handle(self, *args, **kwargs):
        action = Genre.objects.create(name="Action")
        comedy = Genre.objects.create(name="Comedy")
        drama = Genre.objects.create(name="Drama")

        movie1 = Movie.objects.create(
            title="Action Movie",
            description="An exciting action movie.",
            release_date=date(2022, 1, 1),
            poster_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRy7IhZOKmI2NDKOcNuQifBzsNtVNgBzBIoTA&s"
        )
        movie1.genres.add(action)

        movie2 = Movie.objects.create(
            title="Comedy Movie",
            description="A funny comedy movie.",
            release_date=date(2021, 5, 15),
            poster_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIIrFXyJAjfCD8awrkAzJ4zWk6haUwb4l5yQ&s"
        )
        movie2.genres.add(comedy)

        movie3 = Movie.objects.create(
            title="Drama Movie",
            description="A touching drama movie.",
            release_date=date(2023, 3, 10),
            poster_url="https://marketplace.canva.com/EAFBNkVxsJY/1/0/1131w/canva-grey-white-elegant-vintage-drama-movie-poster-Aj9bV_GaoAI.jpg"
        )
        movie3.genres.add(drama)

        self.stdout.write(self.style.SUCCESS('Successfully added initial movie data'))
