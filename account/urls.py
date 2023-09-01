from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *
from . import views
from .forms import Signup_form

urlpatterns = [
    path('login/', Signin_View.as_view()),
    path('signup/', Signup_View.as_view()),
    path('profile/', views.User_Profile, name="users_profile"),
]