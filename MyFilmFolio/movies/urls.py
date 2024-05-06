from django.urls import path
from .views import movie_detail
from cast.views import cast_view

urlpatterns = [
    path('<int:movie_id>/', movie_detail, name='movie_detail'),
    path('cast/<int:cast_id>/', cast_view, name='cast-view')
]