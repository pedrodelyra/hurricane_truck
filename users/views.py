from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from forms import SignupForm

def index(request):
	if request.user.is_authenticated():
		return redirect('microposts.views.index')
	else:
		return render(request, 'users/index.html')

def new(request):
	if request.user.is_authenticated():
		return redirect('microposts.views.index')
	elif request.POST:
		signup_form = SignupForm(request.POST)
		if signup_form.is_valid():
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password']
			password_confirmation = request.POST['password_confirmation']
			User.objects.create_user(username=username, email=email, password=password)
			user = authenticate(username=username, password=password)
			login(request, user)
			return render(request, 'microposts/index.html', {'current_user' : request.user})

		return render(request, 'users/index.html', {'signup_form_errors' : signup_form.errors})
	else:
		return render(request, 'users/index.html')	

def signin(request):
	if request.user.is_authenticated():
		return redirect('microposts.views.index')
	elif request.POST:
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('microposts.views.index')

		signin_form_errors = {'username' : 'Invalid username or password'}
		return render(request, 'users/index.html', {'signin_form_errors' : signin_form_errors})
	else:
		return render(request, 'users/index.html')

def signout(request):
	logout(request)
	return redirect('users.views.index')	
