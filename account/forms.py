from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser


class Signup_form(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "last_name",
            "first_name",
            "age",
            "email",
            "username",
            "password",
            "password2"
        ]
        widgets = {
            "password": forms.PasswordInput(),
            "password2": forms.PasswordInput()
        }


class Signin_form(AuthenticationForm):
    class Meta:
        model: CustomUser
        fields = ["username", "password", "password2"]
        widgets = {
            "password": forms.PasswordInput(),
            "password2": forms.PasswordInput()
        }
        labels = {
            "username": "Nom d'Utilisateur",
            "password": "Mot de passe",
            "password2": "Répeter mot de passe"
        }
