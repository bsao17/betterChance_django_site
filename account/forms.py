from django import forms
from .models import Signup


class Signup_form(forms.ModelForm):
    class Meta:
        model = Signup
        fields = [
            "last_name",
            "first_name",
            "age",
            "email",
            "username",
            "password"
        ]
        widgets = {
            "password": forms.PasswordInput()
        }
