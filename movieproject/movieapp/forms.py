from django import forms
from .models import movie_table

class update_form(forms.ModelForm):
    class Meta:
        model=movie_table
        fields=['name','dis','year','img',]
