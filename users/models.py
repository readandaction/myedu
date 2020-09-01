from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_CHOICES = ((GENDER_MALE, "Male"), (GENDER_FEMALE, "Female"))
    birth = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
