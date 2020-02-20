from django import forms
from . import models

class loginForm(forms.Form):
	name = forms.CharField(max_length=100)
	email = forms.EmailField()