from django.shortcuts import render

from .models import Color, Product, ProductColor

# Create your views here.


def products(request):
    prods = Product.objects.all()
    # Attach all colors for each product (Manual table join in python)
    prods_colors = ProductColor.objects.all()
    for prod in prods:
        prod.colors = [
            x.color_fk.name for x in prods_colors if x.product_fk.name == prod.name
        ]
    return render(request, "inventory/products.html", context={"products": prods})
