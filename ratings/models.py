from __future__ import unicode_literals

from django.db import models
from microposts.models import Micropost
from django.core.validators import MinValueValidator, MaxValueValidator

class Rating(models.Model):
	rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	micropost = models.ForeignKey(Micropost, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.rating)

def avrg_rating(self):
	ratings_set = self.rating_set.all()
	avrg = 0
	for rating in ratings_set:
		avrg += rating.rating
	return avrg / max(1.0, float(len(ratings_set)))

Micropost.avrg_rating = avrg_rating
