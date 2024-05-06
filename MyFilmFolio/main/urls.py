from django.urls import path
from movies.views import movie_detail
from .views import  home

urlpatterns = [
    path('', home, name='home'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_detail'),
]