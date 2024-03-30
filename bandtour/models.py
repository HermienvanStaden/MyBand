from django.db import models

# Create a model for the Post class representing an item on the tour list

# Create your models here.
class Post(models.Model):
    """This is a class representation of a tour Post entry.
        :param location: A location for a band performance location. 
            This is a str with maximum length of 40 characters, 
            defaults to None
        :type location: str, optional
        :param venue: The venue name where the band is performing.
            This is a str with maximum length of 100 characters, 
            defaults to None
        :type venue: str, optional
        :param date: Date of band performance
        :type date: DateField, optional
        :param time: Time of band performance, defaults to None
        :type time: Timefield, optional
        :param tickets: Details on ticket availability. This is a 
            str with maximum length of 100 characters, defaults 
            to None
        :type tickets: str, optional
    """
    location = models.CharField(max_length=40)
    venue = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    tickets = models.CharField(max_length=100)
