from django.shortcuts import render, get_object_or_404
from .models import Cast

def cast_view(request, cast_id):
    cast = get_object_or_404(Cast, cast_id=cast_id)
    return render(request, 'actors.html', {'cast': cast})