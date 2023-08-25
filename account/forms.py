from django import forms

class Signup(forms.Form):
    firstname = forms.CharField(label="Prénom")
    lastname = forms.CharField(label="Nom")
    login = forms.CharField(label="Nom d'utilisateur")
    password = forms.PasswordInput()

class Signin(forms.Form):
    login = forms.CharField(label="Nom d'utilisateur")
    password = forms.PasswordInput()
    repeat_password = forms.PasswordInput()