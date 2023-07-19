from django import forms 
from .models import Tweet, Publicacion

class TweetForm(forms.ModelForm):
    cuerpo = forms.CharField(required = True)

    class Meta:
        model = Tweet
        fields = ["cuerpo"]