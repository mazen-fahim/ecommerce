from django.contrib import admin

from .models import Product, Tag  # import your models

admin.site.register(Product)
admin.site.register(Tag)
