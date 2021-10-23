from . import models
from django import forms


class CreatArticle (forms.ModelForm):
    class Meta:
        model=models.Article
        fields=['title','slug','body','image']
