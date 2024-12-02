from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        return HttpResponse(f"Пользователь, {name} с номером {phone}! Ваше сообщение получено.")
    return render(request, 'contacts.html')


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)



