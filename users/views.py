from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from forms import SignupForm
from users.models import Follower, Profile

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
			new_user = User.objects.create_user(username=username, email=email, password=password)
			user_profile = Profile(user=new_user)
			user_profile.save()
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

def user(request, user_id):
	if request.user.is_authenticated():
		visited_user = User.objects.get(id=user_id)
		print("lala:")
		print(visited_user.profile.followers())
		print(len(visited_user.profile.followers()))
		return render(request, 'users/user.html', {'current_user': request.user, 'visited_user': visited_user, 'microposts': visited_user.micropost_set.order_by('-pub_date')[:5], 'followers_num': len(visited_user.profile.followers()), 'following_num': len(visited_user.profile.following()), 'microposts_num': visited_user.micropost_set.all().count})
	else:
		return render(request, 'users/index.html')

def follow(request, following_id):
	if request.user.is_authenticated():
		visited_user = User.objects.get(id=following_id)
		follower_user = request.user
		following_user = User.objects.get(id=following_id)
		f = Follower(follower=follower_user, followed=following_user)
		f.save()
		return render(request, 'users/user.html', {'current_user': request.user, 'visited_user': visited_user, 'microposts': visited_user.micropost_set.order_by('-pub_date')[:5], 'followers_num': len(visited_user.profile.followers()), 'following_num': len(visited_user.profile.following()), 'microposts_num': visited_user.micropost_set.all().count})
	else:
		return render(request, 'users/index.html')

def unfollow(request, unfollowing_id):
	if request.user.is_authenticated():
		visited_user = User.objects.get(id=unfollowing_id)
		follower_user = request.user
		unfollowing_user = User.objects.get(id=unfollowing_id)
		f = Follower.objects.get(follower=follower_user, followed=unfollowing_user)
		f.delete()
		return render(request, 'users/user.html', {'current_user': request.user, 'visited_user': visited_user, 'microposts': visited_user.micropost_set.order_by('-pub_date')[:5], 'followers_num': len(visited_user.profile.followers()), 'following_num': len(visited_user.profile.following()), 'microposts_num': visited_user.micropost_set.all().count})
	else:
		return render(request, 'users/index.html')

