from django import forms
from .models import *

class HomeForm(forms.ModelForm):
    post = forms.CharField();

    class Meta:
        model = Comment
        exclude = ('submit',)