from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from inventory.models import Product

# Create your views here.


# def index(request):
#     return render(request, "dashboard/index.html")


class Products(ListView):
    model = Product
    template_name = "dashboard/index.html"
    context_object_name = "products"


class CreateProduct(CreateView):
    fields = "__all__"
    model = Product
    template_name = "dashboard/create.html"
    success_url = reverse_lazy("dashboard:index")


class UpdateProduct(UpdateView):
    fields = "__all__"
    model = Product
    template_name = "dashboard/update.html"
    success_url = reverse_lazy("dashboard:index")


class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy("dashboard:index")
