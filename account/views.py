from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import CustomUser
from betterChanceSite import settings
from .forms import Signin_form
from .models import Profile


def login_user(request):
    form = Signin_form
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if form.is_valid:
            login(request, user)
            return render(request, 'users/profile.html')
        else:
            message = messages.info(request, "login ou mot de passe incorrect, veuillez réessayer !")
            return redirect("login")
    return render(request, "account_views/login.html", context={"form": form})


def logout_user(request):
    logout(request)
    return render(request, 'betterChance_views/index.html')


class CustomManagerForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields


def signup(request):
    context = {}
    if request.method == 'POST':
        form = CustomManagerForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request, "users/profile.html")
        else:
            message = messages.info(request, "erreur dans les information, veuillez recommencer !")
            context['error'] = form.errors
            return render(request, "account_views/signup.html")
    form = UserCreationForm()
    context['error'] = form.errors
    return render(request, "account_views/signup.html", context={"form": form})


def User_Profile(request):
    avatar = Profile.avatar
    return render(request, "users/profile.html", context={"avatar": avatar})
