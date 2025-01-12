from django.shortcuts import render
from .models import Movie
from django.core.serializers import serialize
import json

def movie_list(request):
    # Fetch all movies ordered by release year
    movies = Movie.objects.all().order_by('-released_year')

    # Serialize the movie data to pass it to the template
    movie_data = list(movies.values('released_year', 'imdb_rating'))

    # Return the template with the context
    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'movie_data': json.dumps(movie_data)  # Passing data as JSON string
    })