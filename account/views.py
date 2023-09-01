from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import *
from .models import Profile


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return render(request, 'users/profiles')
        else:
            login(request, user)
            return HttpResponse('Erreur de connexion, veuillez recommencer !')


class Signin_View(TemplateView):
    template_name = "account_views/login.html"
    success_url = login_user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["signin_form"] = AuthenticationForm
        return context


class Signup_View(TemplateView):
    template_name = "account_views/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["signup_form"] = Signup_form
        return context


def User_Profile(request):
    avatar = Profile.avatar
    return render(request, "users/profile.html", context={"avatar": avatar})
