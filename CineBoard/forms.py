from django import forms
from . import models



class FilmsForm(forms.ModelForm):
    class Meta:
        model = models.Films
        fields = '__all__'
