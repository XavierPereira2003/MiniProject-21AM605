from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from movies.models import Movies
from .models import Users,movieReview,favCast
from django.shortcuts import get_object_or_404
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:home')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main:home')  # redirect to a home page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('main:home')





def reviewMovie(request, user_id):
    user = get_object_or_404(Users, user__id=user_id)
    username = user.user.username
    reviews_by_user = movieReview.objects.filter(user=user).select_related('movie')  # Join with the movie
    return render(request, 'reviews.html', {'username': username, 'reviews': reviews_by_user})
