from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser


class Signup_form(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "password"
        ]
        widgets = {
            "password": forms.PasswordInput()
        }


class Signin_form(AuthenticationForm):
    class Meta:
        model: CustomUser
        fields = ["username", "password"]
        widgets = {
            "password":forms.PasswordInput(),
        }
        labels = {
            "username": "Nom d'utilisateur",
            "password": "Mot de passe",
        }
