from .models import Review, Movie

def recommend_movies(user):
    user_reviews = Review.objects.filter(user=user)
    if not user_reviews.exists():
        return Movie.objects.none()

    user_movie_ids = user_reviews.values_list('movie_id', flat=True)
    similar_users = Review.objects.filter(movie_id__in=user_movie_ids).exclude(user=user).values_list('user_id', flat=True)
    similar_user_reviews = Review.objects.filter(user_id__in=similar_users).exclude(movie_id__in=user_movie_ids)

    recommended_movie_ids = similar_user_reviews.values_list('movie_id', flat=True).distinct()
    return Movie.objects.filter(id__in=recommended_movie_ids)
