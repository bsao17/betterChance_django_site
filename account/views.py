from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from .forms import Signin_form, Signup_form
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
            login(request, user)
            return redirect("login")
    return render(request, "account_views/login.html", context={"form": form})


def logout_user(request):
    logout(request)
    return render(request, 'betterChance_views/index.html')


def signup(request):
    form = UserCreationForm
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
    return render(request, "account_views/signup.html", context={"form": form})

# class Signup_View(TemplateView):
#     template_name = "account_views/signup.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["signup_form"] = Signup_form
#         return context


def User_Profile(request):
    avatar = Profile.avatar
    return render(request, "users/profile.html", context={"avatar": avatar})
