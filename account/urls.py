from django.urls import path, include
from . import views

app_name = 'account'
urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name="logout"),
    path('profile/', views.User_Profile, name="profile"),
]