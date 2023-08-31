from django.urls import path, include
from .views import Signup_View
from . import views
from .forms import Signup_form

urlpatterns = [
    path('signin/', views.signin),
    path('signup/', Signup_View.as_view()),
]