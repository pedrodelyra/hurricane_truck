from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

	def followers(self):
		followers_set = []
		following_set = Follower.objects.filter(followed=self.user)
		for f in following_set:
			followers_set.append(f.follower)
		return followers_set

	def following(self):
		following_set = []
		followers_set = Follower.objects.filter(follower=self.user)
		for f in followers_set:
			following_set.append(f.followed)
		return following_set

	def feed(self):
		following_set = self.following()
		microposts = self.user.micropost_set.all()
		for following in following_set:
			microposts = microposts | following.micropost_set.all()
		return microposts.order_by('-pub_date')[:10]

	def __str__(self):
		return "%s's profile" % self.user

class Follower(models.Model):
	follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
	followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')
