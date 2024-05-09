from math import log
from django.shortcuts import render, get_object_or_404
from .models import Movies
from users.models import Users,movieReview

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movies, movie_id=movie_id)
    return render(request, 'movies.html', {'movie': movie})


def postReview(request):
    if request.method == 'POST':
        user = request.user
        movie_id = request.POST.get('movie_id')
        
        movie = get_object_or_404(Movies, movie_id=movie_id)
        movieReview.objects.create(user=user, movie=movie, review=review)
        return render(request, 'movies.html', {'movie': movie})
