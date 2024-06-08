from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, movie_list_view, movie_detail_view

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', movie_list_view, name='movie_list'),
    path('<int:pk>/', movie_detail_view, name='movie_detail'),
]
