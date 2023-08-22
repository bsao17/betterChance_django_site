import datetime

from django.shortcuts import render


# Create your views here.
def orders(request):
    return render(request, "order_views/form.html", context={"date": datetime.date.today()})
