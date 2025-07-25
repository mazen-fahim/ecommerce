from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxLengthValidator
from django.db import models

# Create your models here.

color_choices = {
    "red": "red",
    "green": "green",
    "blue": "blue",
    "white": "white",
    "brown": "brown",
    "cyan": "cyan",
    "black": "black",
}

material_choices = {
    "Wool": "Wool",
    "Cashmere": "Cashmere",
    "Cotton": "Cotton",
    "Silk": "Silk",
    "Linen": "Linen",
}

tag_choices = {
    "Power": "Power",
    "Velvet": "Velvet",
    "Sleek": "Sleek",
    "Drift": "Drift",
    "Wool": "Wool",
    "Heritage": "Heritage",
    "Phantom": "Phantom",
}


class Tag(models.Model):
    name = models.CharField(
        max_length=100, null=False, blank=False, choices=list(tag_choices.items())
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    description = models.TextField(
        null=False, blank=False, validators=[MaxLengthValidator(100)]
    )
    material = models.CharField(
        max_length=20, null=False, blank=False, choices=list(material_choices.items())
    )
    # TODO: Make a custom validator that makes sure that (size is \d\d\w)
    size = models.CharField(max_length=3, null=False, blank=False)
    colors = ArrayField(
        models.CharField(
            max_length=20, null=False, blank=False, choices=list(color_choices.items())
        ),
        size=10,
    )

    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to="uploads/%Y/%m/%d", null=True)

    def __str__(self):
        return str(self.name)
