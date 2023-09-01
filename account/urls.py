from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *
from . import views
from .forms import Signup_form

urlpatterns = [
    path('signin/', Signin_View.as_view()),
    path('signup/', Signup_View.as_view()),
    path('profile/', Profile.as_view(), name="users_profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)