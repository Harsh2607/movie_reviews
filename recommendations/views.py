from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .utils import recommend_movies
from movies.serializers import MovieSerializer

class MovieRecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        recommended_movies = recommend_movies(request.user)
        serializer = MovieSerializer(recommended_movies, many=True)
        return Response(serializer.data)
