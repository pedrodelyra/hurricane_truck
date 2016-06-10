from django.shortcuts import render

def index(request):
	return render(request, 'users/index.html')

def new(request):
	return render(request, 'users/new.html')
