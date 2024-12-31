from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import ProductForm
from .models import Category, Product
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ContactTemplateView(TemplateView):
    template_name = "catalog/contact.html"

    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            return HttpResponse(f"Пользователь, {name} с номером {phone}! Ваше сообщение получено.")
        return render(request, 'contact.html')
