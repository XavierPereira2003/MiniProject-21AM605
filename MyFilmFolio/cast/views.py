from django.shortcuts import render
from . import models

# Create your views here.
def actor_list(request):
    actors = models.Cast.objects.all()
    return render(request, 'cast/actor_list.html', {'actors': actors})