from django.views.generic import TemplateView
from .forms import *


# Create your views here.
class Signin_View(TemplateView):
    template_name = "account_views/signin.html"

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
