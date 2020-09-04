from django import forms
from . import models

class Create(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['topic', 'body', 'slug']
