from django.shortcuts import render, redirect
from django.utils import timezone
from forms import MicropostForm

def index(request):
	if request.user.is_authenticated():
		return render(request, 'microposts/index.html', {'current_user' : request.user })
	else:
		return render(request, 'users/index.html') 

def new_micropost(request):
	if request.POST and request.user.is_authenticated():
		micropost_form = MicropostForm(request.POST)
		if micropost_form.is_valid():
			current_user = request.user
			current_user.micropost_set.create(content=request.POST['content'], pub_date=timezone.now())
		return render(request, 'microposts/index.html', {'current_user' : request.user })
	else:
		return redirect('microposts.views.index')
