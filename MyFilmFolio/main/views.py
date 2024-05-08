from django.shortcuts import render
from movies.models import Movies, Genre
from cast.models import Cast
from django.db.models import Q


def home(request):
    # Fetching popular movies based on vote average
    popular_movies = Movies.objects.order_by('-vote_average')[:10]

    featured_movies = Movies.objects.order_by('?')[:10]

    latest_movies = Movies.objects.order_by('-release_date')[:10]

    genres = Genre.objects.all()

    context = {
        'popular_movies': popular_movies,
        'featured_movies': featured_movies,
        'latest_movies': latest_movies,
        'genres': genres,
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

def movies_by_genre(request, genre):
    # Retrieve movies belonging to the specified genre
    genre_movies = Movies.objects.filter(genre__genre=genre)

    context = {
        'genre_movies': genre_movies,
        'genre': genre,
    }

    return render(request, 'movies_by_genre.html', context)


def cast_search(request):
    return render(request, 'cast_search.html')


def cast_search_results(request):
    results = []
    query = request.GET.get('q')

    if query:
        results = Cast.objects.filter(Q(name__icontains=query))

    context = {
        'results': results,
    }

    return render(request, 'cast_search.html', context)