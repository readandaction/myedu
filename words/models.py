from django.db import models


class Word(models.Model):

    """ Word Model Definition """

    name = models.CharField(max_length=10)
    pronounce = models.CharField(max_length=30)
    meaning = models.TextField(max_length=30)