from django.db import models
from django.urls import reverse

class Blog(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blogs:detail')
