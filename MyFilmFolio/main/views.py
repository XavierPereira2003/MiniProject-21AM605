from django.shortcuts import render
from movies.models import Movies


def home(request):
    # Fetching popular movies based on vote average
    popular_movies = Movies.objects.order_by('-vote_average')[:6]

    # Fetching random movies for featured section
    featured_movies = Movies.objects.order_by('?')[:6]

    # Fetching latest movies based on release date
    latest_movies = Movies.objects.order_by('-release_date')[:6]

    context = {
        'popular_movies': popular_movies,
        'featured_movies': featured_movies,
        'latest_movies': latest_movies,
    }

    return render(request, 'home.html', context)
