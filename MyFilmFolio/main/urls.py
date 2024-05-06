from django.urls import path
from movies.views import movie_detail
from .views import home, search, search_results

urlpatterns = [
    path('', home, name='home'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('search/', search, name='search'),  # URL for the search page
    path('search/results/', search_results, name='search_results'),
]
