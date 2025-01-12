from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy

class ProductListView(ListView):
    model = Product
    paginate_by = 3

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')

class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product_detail"
    template_name = "crud/product_detail.html"

