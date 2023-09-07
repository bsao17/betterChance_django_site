from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        verbose_name = "email"


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.last_name + " " + self.user.first_name
