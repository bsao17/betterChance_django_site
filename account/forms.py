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
            "username"
        ]
        widgets = {
            "password": forms.PasswordInput()
        }

    def clean(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        print(password, password2)


class Signin_form(AuthenticationForm):
    class Meta:
        model: CustomUser
        fields = ["username", "password"]
        widgets = {
            "password": forms.PasswordInput(),
        }
        labels = {
            "username": "Nom d'Utilisateur",
            "password": "Mot de passe",
        }
