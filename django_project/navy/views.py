from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import TemplateView , View

from django.http import HttpResponse


class NavyViews(TemplateView):
	template_name = "navy/home.html"

	def get(self,request):
		context = {}
		context['data'] = {"navy_empname":"rajesh"}
		context['blog'] ={"navy_salary":"ghjgjh"}
		return render(request,self.template_name,context)

