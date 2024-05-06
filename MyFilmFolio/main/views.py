from django.shortcuts import render
from movies.models import Movies
from django.db.models import Q


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


def search(request):
    return render(request, 'search.html')

def search_results(request):
    query = request.GET.get('q')

    if query:
        results = Movies.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        results = []

    context = {
        'results': results,
    }

    return render(request, 'search.html', context)

