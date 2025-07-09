from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from inventory.models import Product, Tag

# Create your views here.


# def index(request):
#     return render(request, "dashboard/index.html")


class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        from django.http import HttpResponseForbidden
        from django.template import loader

        template = loader.get_template("dashboard/forbidden.html")
        context = {}  # Add any context you want here
        return HttpResponseForbidden(template.render(context, self.request))


class Products(SuperuserRequiredMixin, ListView):
    model = Product
    template_name = "dashboard/index.html"
    context_object_name = "products"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()

        # 1. Filter Search
        name = self.request.GET.get("search")
        if name:
            queryset = queryset.filter(name__icontains=name)

        # 2. Filter Tags
        tag_name = self.request.GET.get("tag")
        if tag_name and tag_name != "Any":
            tag = Tag.objects.filter(name__iexact=tag_name).first()
            if tag:
                queryset = queryset.filter(tags=tag)  # TODO: Understand this
        return queryset

    def get_paginate_by(self, queryset):
        limit = self.request.GET.get("limit")
        if limit and limit.isdigit():
            return int(limit)
        return self.paginate_by


class CreateProduct(SuperuserRequiredMixin, CreateView):
    fields = "__all__"
    model = Product
    template_name = "dashboard/create.html"
    success_url = reverse_lazy("dashboard:index")


class UpdateProduct(SuperuserRequiredMixin, UpdateView):
    fields = "__all__"
    model = Product
    template_name = "dashboard/update.html"
    success_url = reverse_lazy("dashboard:index")


class DeleteProduct(SuperuserRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("dashboard:index")
