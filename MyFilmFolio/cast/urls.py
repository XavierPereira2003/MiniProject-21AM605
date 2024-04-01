from django.urls import path
from . import views

urlpatterns = [
    path('cast/',views.actor_list, name='cast'),
    path("cast/<>")
]