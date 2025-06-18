from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Product

# Create your views here.


# def products(request):
#     prods = Product.objects.all()
#     # Attach all colors for each product (Manual table join in python)
#     prods_colors = ProductColor.objects.all()
#     for prod in prods:
#         prod.colors = [
#             x.color_fk.name for x in prods_colors if x.product_fk.name == prod.name
#         ]
#     return render(request, "inventory/products.html", context={"products": prods})


# Here I defined a class that inherits from a ListView class
# This class will generate a callable object that will be used to handle
# the request
# HttpRequest -> Callable Object -> HttpResponse
#                     ^
#                class or func
class Products(ListView):
    model = Product
    template_name = "inventory/index.html"
    context_object_name = "products"


class Details(DetailView):
    model = Product
    template_name = "inventory/details.html"
    context_object_name = "product"
