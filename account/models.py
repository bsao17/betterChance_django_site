from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser
from django.db import models
import betterChanceSite


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "User"

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, default='default.jpg', upload_to='account/profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
