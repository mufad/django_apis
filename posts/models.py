from django.db import models

# Create your models here.

class Post(models.Model):
	author = models.CharField(max_length=250)
	title = models.CharField(max_length=250)

	def __str__(self):
		return self.title + '--'+ self.author