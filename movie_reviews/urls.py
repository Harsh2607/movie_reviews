from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from authentication.views import UserRegistrationView, UserLoginView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import redirect_to_swagger, index


schema_view = get_schema_view(
    openapi.Info(
        title="Movie Reviews API",
        default_version='v1',
        description="API for managing movie reviews and recommendations",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('movies/', include('movies.urls')),
    path('reviews/', include('reviews.urls')),
    path('api/movies/', include('movies.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/recommendations/', include('recommendations.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', UserRegistrationView.as_view(), name='register'),
    path('auth/login/', UserLoginView.as_view(), name='login'),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', index, name='index'),
]
