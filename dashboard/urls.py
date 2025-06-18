from django.urls import path

from . import views

# This is used to establish a namespce.
# Any path name that is defined here will be preappended by dashboard_
# automatically by django if I want to referce this url it will be like thi
# {% url dashboard:index %}
app_name = "dashboard"
urlpatterns = [
    path("", views.Products.as_view(), name="index"),
    path("create/", views.CreateProduct.as_view(), name="create"),
    path("update/<int:pk>", views.UpdateProduct.as_view(), name="update"),
    path("delete/<int:pk>", views.DeleteProduct.as_view(), name="delete"),
]
