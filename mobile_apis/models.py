from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=25)
    author = models.CharField(max_length=25)

    def __str__(self):
        return self.title