from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^signup/$', views.new, name='signup'),
	url(r'^signin/$', views.signin, name='signin'),
	url(r'^signout/$', views.signout, name='signout'),
    url(r'^(?P<user_id>[0-9]+)/$', views.user, name='user'),
	url(r'^follow/(?P<following_id>[0-9]+)/$', views.follow, name='follow'),
	url(r'^unfollow/(?P<unfollowing_id>[0-9]+)/$', views.unfollow, name='unfollow'),
]

