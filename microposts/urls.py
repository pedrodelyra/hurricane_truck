from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^new_micropost/$', views.new_micropost, name='new_micropost'),
	url(r'^microposts/$', views.microposts, name='microposts'),
    url(r'^microposts/(?P<micropost_id>[0-9]+)/$', views.show, name='show'),
]
