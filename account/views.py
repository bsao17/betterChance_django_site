from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView

from .forms import *


# Create your views here.
def signin(request):
    form = Signin_form(request.POST)
    if form.is_valid():
        return render(request, "orders_views/order_form.html")
    else:
        print("error connect")
        return render(request, "account_views/signin.html", context={"signin_form": form})


class Signup_View(TemplateView):
    template_name = "account_views/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["signup_form"] = Signup_form
        return context
