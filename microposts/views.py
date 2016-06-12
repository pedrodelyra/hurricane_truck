from django.shortcuts import render

def index(request):
	if request.user.is_authenticated():
		return render(request, 'microposts/index.html', {'current_user' : request.user})
	else:
		return render(request, 'users/index.html') 
