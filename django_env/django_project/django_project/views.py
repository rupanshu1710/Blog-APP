from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<h1>Django_project_Home</h1>')
def about(request):
	return HttpResponse('<h1>Django_project About')