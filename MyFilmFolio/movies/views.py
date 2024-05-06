from django.shortcuts import render, get_object_or_404
from .models import Movies

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movies, movie_id=movie_id)
    return render(request, 'movies.html', {'movie': movie})