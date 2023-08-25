from django.shortcuts import render, HttpResponse, redirect
from .forms import *

# Create your views here.
def signin(request):
    return render(request, "account_views/signin.html")

def signup(request):
    form = Signup(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            return redirect("orders_views/form.html")
    return render(request, "account_views/signup.html", context={"form": form})