from django.db import models

class Author(models.Model):

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=1, choices= GENDER_CHOICES, default=MALE)

    def __str__(self):
        return self.lastname + " " + self.firstname