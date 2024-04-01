from django.urls import path
from . import views

app_name='cast'
urlpatterns = [
    path('cast/',views.actor_list, name='cast_home'),
    path("cast/<slug>:slug", views.view_actor, name="cast_detail"),
]