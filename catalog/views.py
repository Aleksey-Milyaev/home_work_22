from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product
from django.views.generic import DetailView, ListView, TemplateView


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactTemplateView(TemplateView):
    template_name = "catalog/contact.html"

    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            return HttpResponse(f"Пользователь, {name} с номером {phone}! Ваше сообщение получено.")
        return render(request, 'contact.html')
