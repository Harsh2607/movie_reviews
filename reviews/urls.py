from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, review_list_view, add_review_view

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('movies/<int:movie_id>/reviews/', review_list_view, name='review_list'),
    path('movies/<int:movie_id>/reviews/add/', add_review_view, name='add_review'),
]