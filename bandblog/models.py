from django.db import models

# Create a model for the Post class representing a blog post

# Create your models here.
class Post(models.Model):
    """This is a class representation of a simple blog entry.
    :param title: A title for a blog post. This is a string 
        with maximum length of 140 characters, defaults to
        None
    :type title: str, optional
    :param body: The body text of the blog post. It has no
        length restrictions, defaults to None
    :type body: str, optional
    :param date: Date of blog post entry Format of date is 
        "Y-m-d", defaults to current date
    :type date: str, optional
    """
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

def __str__(self):
    """The method that sets how a Post class object is displayed.
        
        :return: Blog post title, defaults tot None
        :rtype: Charfield, optional
    """
    return self.title