from django.urls import path

from . import views

app_name = "inventory"
urlpatterns = [
    path("", views.Products.as_view(), name="index"),
    path("details/<int:pk>", views.Details.as_view(), name="details"),
]
