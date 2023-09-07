from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *
from . import views
from .forms import Signup_form

app_name = 'account'
urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('signup/', Signup_View.as_view(), name='signup'),
    path('profile/', views.User_Profile, name="profile"),
]