from django.urls import path
from .views import home
from movies.views import movie_detail

urlpatterns = [
    path('', home, name='home'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_detail'),
]