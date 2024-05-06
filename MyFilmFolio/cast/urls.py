from django.urls import path
from . import views
from movies.views import movie_detail


app_name='cast'
urlpatterns = [
    path('<int:cast_id>/', views.cast_view, name='cast-view'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_detail'),
]