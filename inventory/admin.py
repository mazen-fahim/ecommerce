from django.contrib import admin

from .models import Color, Product, ProductColor  # import your models

admin.site.register(Product)
admin.site.register(ProductColor)
admin.site.register(Color)
