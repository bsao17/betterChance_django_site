from django.urls import path, include
from .views import *
from . import views
from .forms import Signup_form

urlpatterns = [
    path('signin/', Signin_View.as_view()),
    path('signup/', Signup_View.as_view()),
]