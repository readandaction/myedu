from django.db import models


class Book(models.Model):

    """ Book Model Definition"""

    title = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self):
        return self.title