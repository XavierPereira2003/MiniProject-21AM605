from django import forms
from .models import movieReview

class RatingForm(forms.ModelForm):
    class Meta:
        model = movieReview
        fields = ['review']