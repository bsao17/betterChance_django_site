from django.shortcuts import render


# Create your views here.
def detail(request):
    #detailexplain = {"one": "explication", "two": "machine learning", "three": "data-science", "four": "algorithme"}
    return render(request, "explanations_views/index.html")
