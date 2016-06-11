from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home/$', views.home, name='home'),
	url(r'^signup/$', views.new, name='signup'),
	url(r'^signin/$', views.signin, name='signin'),
	url(r'^signout/$', views.signout, name='signout'),
]

