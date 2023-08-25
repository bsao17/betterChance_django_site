from django.shortcuts import render

# Create your views here.
def signin(request):
    return render(request, "account_views/signin.html")

def signup(request):
    return render(request, "account_views/signup.html")