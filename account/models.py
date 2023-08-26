from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
class Signup(AbstractUser):
    age = models.CharField(max_length=3, blank=True)
