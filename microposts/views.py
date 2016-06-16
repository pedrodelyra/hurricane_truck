from django.shortcuts import render, redirect
from django.utils import timezone
from forms import MicropostForm

def index(request):
	if request.user.is_authenticated():
		return render(request, 'microposts/index.html', {'current_user' : request.user, 'feed' : request.user.profile.feed()})
	else:
		return render(request, 'users/index.html') 

def new_micropost(request):
	if request.POST and request.user.is_authenticated():
		micropost_form = MicropostForm(request.POST)
		if micropost_form.is_valid():
			current_user = request.user
			current_user.micropost_set.create(content=request.POST['content'], pub_date=timezone.now())
		return render(request, 'microposts/index.html', {'current_user' : request.user, 'feed' : request.user.profile.feed()})
	else:
		return redirect('microposts.views.index')

def microposts(request):
	if request.user.is_authenticated():
		return render(request, 'microposts/microposts.html', {'current_user' : request.user, 'microposts' : request.user.micropost_set.order_by('-pub_date')[:5]})
	else:
		return render(request, 'users/index.html')

def show(request, micropost_id):
	if request.user.is_authenticated():
		return render(request, 'microposts/micropost.html', {'current_user' : request.user, 'micropost' : request.user.micropost_set.get(id=micropost_id)})
	else:
		return render(request, 'users/index.html')
