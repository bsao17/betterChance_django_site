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
        fields = ["username", "password1", "password2"]
        widgets = {
            "password1": forms.PasswordInput(),
            "password2": forms.PasswordInput(),
        }
        labels = {
            "username": "Nom d'utilisateur",
            "password1": "Mot de passe",
            "password2": "répéter mot de passe"
        }
