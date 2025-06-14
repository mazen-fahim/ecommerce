from django.db import models

# Create your models here.


class ProductColor(models.Model):
    product_fk = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)
    color_fk = models.ForeignKey("Color", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        product_name = self.product_fk.name if self.product_fk else "No Product"
        color_name = self.color_fk.name if self.color_fk else "No Color"
        return f"{product_name} - {color_name}"


class Color(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name
