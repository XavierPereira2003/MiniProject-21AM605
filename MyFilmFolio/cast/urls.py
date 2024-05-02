from django.urls import path
from . import views

app_name='cast'
urlpatterns = [
    path('',views.listActors, name='cast_home'),
    # path("<slug>:slug", views.view_actor, name="cast_detail"),
]