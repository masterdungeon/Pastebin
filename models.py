from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Paste(models.Model):
	content = models.CharField(max_length = 10000000)
	url = models.CharField(max_length = 32, unique =True)
	

	def __str__(self):
		return (self.url)