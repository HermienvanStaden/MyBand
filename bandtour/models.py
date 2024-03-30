from django.db import models

# Create a model for the Post class representing an item on the tour list

# Create your models here.
class Post(models.Model):
    location = models.CharField(max_length=40)
    venue = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    tickets = models.CharField(max_length=100)

""" def __str__(self):
    return self.location """
