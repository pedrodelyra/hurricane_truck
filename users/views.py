from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from forms import SignupForm

def index(request):
	if request.user.is_authenticated():
		return redirect('users.views.home')
	else:
		return render(request, 'users/index.html')

def home(request):
	if request.user.is_authenticated():
		return render(request, 'users/home.html', {'current_user' : request.user})
	else:
		return render(request, 'users/index.html')

def new(request):
	if request.user.is_authenticated():
		return redirect('users.views.home')
	elif request.POST:
		print(request.POST)
		print(request.POST['password'])
		print(request.POST['password_confirmation'])
		signup_form = SignupForm(request.POST)
		if signup_form.is_valid():
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password']
			password_confirmation = request.POST['password_confirmation']
			new_user = User.objects.create_user(username=username, email=email, password=password)
			login(request, user)
			return redirect('users.views.home')

		return render(request, 'users/index.html', {'signup_form_errors' : signup_form.errors})
	else:
		return render(request, 'users/index.html')	

def signin(request):
	if request.user.is_authenticated():
		return redirect('users.views.home')
	elif request.POST:
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('users.views.home')

		signin_form_errors = {'username' : 'Invalid username or password'}
		return render(request, 'users/index.html', {'signin_form_errors' : signin_form_errors})
	else:
		return render(request, 'users/index.html')

def signout(request):
	logout(request)
	return redirect('users.views.index')	
