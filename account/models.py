from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
class CustomUser(AbstractUser):
    age = models.CharField(max_length=3, blank=True)

    class Meta:
        verbose_name = "Utilisateur"

    def __str__(AbstractUser):
        return AbstractUser.last_name + " " + AbstractUser.first_name


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.last_name + " " + self.user.first_name
