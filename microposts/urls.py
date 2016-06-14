from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^new_micropost/$', views.new_micropost, name='new_micropost'),
]
