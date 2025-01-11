# movies/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # Default view for movies
    # Add more URL patterns here (e.g., details pages, search, etc.)
]