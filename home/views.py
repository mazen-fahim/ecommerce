from django.shortcuts import render
from django.views.generic import ListView

from inventory.models import Product

# Create your views here.


def index(request):
    prods = Product.objects.all()
    return render(request, "home/index.html", context={"products": prods[:3]})


def about(request):
    return render(request, "home/about.html")


def contactus(request):
    return render(request, "home/contactus.html")
