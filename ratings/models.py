from __future__ import unicode_literals

from django.db import models
from microposts.models import Micropost
from django.core.validators import MinValueValidator, MaxValueValidator

class Rating(models.Model):
	rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	micropost = models.ForeignKey(Micropost, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.rating)
