from django.shortcuts import render
from django.views.generic import TemplateView

from django.views import View
from . import forms

# Create your views here.

class userLogin(TemplateView):
	template_name = 'base.html'

	def get(self, request):
		form = forms.loginForm()
		return render(request, self.template_name, {'form':form})
