from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Micropost(models.Model):
	content = models.CharField(max_length=150)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.content
