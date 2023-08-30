from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *


# Create your views here.
def signin(request):
    form_signin = Signin_form(request.POST)
    return render(request, "account_views/signin.html", context={"signin_form": form_signin})


def signup(request):
    form = Signup_form(request.POST)
    if form.is_valid():
        form.save()
        return redirect("orders")
    return render(request, "account_views/signup.html", {"signup_form": form})
