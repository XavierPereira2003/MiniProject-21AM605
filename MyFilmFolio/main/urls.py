from django.urls import path
from movies.views import movie_detail
from cast.views import cast_view
from .views import home, search, search_results, movies_by_genre, cast_search, cast_search_results

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('search/movies', search, name='search'),  # URL for the search page
    path('search/movies/results/', search_results, name='search_results'),
    path('genre/<str:genre>/', movies_by_genre, name='movies_by_genre'),
    path('search/cast', cast_search, name='cast_search'),
    path('cast/<int:cast_id>', cast_view, name='cast_view'),
    path('search/cast/results/', cast_search_results, name='cast_search_results'),
]
