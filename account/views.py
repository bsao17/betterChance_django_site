from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .forms import *


# Create your views here.
class Signin_View(LoginView):
    template_name = "account_views/signin.html"
    success_url = reverse_lazy('account/profile/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["signin_form"] = Signin_form
        return context


class Signup_View(TemplateView):
    template_name = "account_views/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["signup_form"] = Signup_form
        return context


class Profile(TemplateView):
    template_name = "users/profile.html"
