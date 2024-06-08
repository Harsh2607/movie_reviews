from django.urls import path
from .views import UserRegistrationView, UserLoginView, LogoutView, register_view, login_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/register/', UserRegistrationView.as_view(), name='api_register'),
    path('api/login/', UserLoginView.as_view(), name='api_login'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),
]
