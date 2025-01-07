from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import ProductForm
from .models import Product
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
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
