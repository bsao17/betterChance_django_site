from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    age = models.CharField(max_length=3, blank=True)
    class Meta:
        verbose_name = "BT_utilisateur"

    def __str__(AbstractUser):
        return AbstractUser.last_name + " " +  AbstractUser.first_name


