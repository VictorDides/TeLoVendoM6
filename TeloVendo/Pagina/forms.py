from django import forms 
from .models import Tweet, Publicacion

class TweetForm(forms.ModelForm):
    cuerpo = forms.CharField(required = True,
                            widget= forms.widgets.Textarea(
                                attrs={
                                    "placeholder":"Escribe aca",
                                    "class": "textarea is-success is-medium"
                                    }
                                ))

    class Meta:
        model = Tweet
        fields = ["cuerpo"]