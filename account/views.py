from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *


# Create your views here.
def signin(request):
    return render(request, "account_views/signin.html")


def signup(request):
    return render(request, "account_views/signup.html")
