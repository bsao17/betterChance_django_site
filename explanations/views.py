from django.shortcuts import render


# Create your views here.
def detail(request):
    detailexplain = ["Explication générale", "machine learning", "data-science", "algorithme"]
    return render(request, "explanations_views/index.html", context={"details": detailexplain})
