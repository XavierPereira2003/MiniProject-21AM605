from math import log
<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from .models import Movies
from users.models import Users,movieReview

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movies, movie_id=movie_id)
    return render(request, 'movies.html', {'movie': movie})


=======

from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movies
from users.models import Users, movieReview
from django.db.models import Avg

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movies, movie_id=movie_id)
    user_rating = None
    if request.user.is_authenticated:
        user = request.user
        try:
            users_instance = Users.objects.get(user=user)
            user_rating_obj = movieReview.objects.filter(user=users_instance, movie=movie).first()
            if user_rating_obj:
                user_rating = user_rating_obj.review
        except Users.DoesNotExist:
            pass
    return render(request, 'movies.html', {'movie': movie, 'user_rating': user_rating})


@login_required
>>>>>>> 7da2e0a85fa2c02ca8bceb5a84247bee13337093
def postReview(request):
    if request.method == 'POST':
        user = request.user
        movie_id = request.POST.get('movie_id')
<<<<<<< HEAD
        
        movie = get_object_or_404(Movies, movie_id=movie_id)
        movieReview.objects.create(user=user, movie=movie, review=review)
        return render(request, 'movies.html', {'movie': movie})
=======
        rating = request.POST.get('rating')

        movie = get_object_or_404(Movies, movie_id=movie_id)
        users_instance, created = Users.objects.get_or_create(user=user)
        try:
            review = movieReview.objects.get(user=users_instance, movie=movie)
        except movieReview.DoesNotExist:
            review = movieReview(user=users_instance, movie=movie)

        review.review = rating
        review.save()

        return redirect('movies:movie_detail', movie_id=movie_id)
>>>>>>> 7da2e0a85fa2c02ca8bceb5a84247bee13337093
