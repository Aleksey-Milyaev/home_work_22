from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        return HttpResponse(f"Пользователь, {name} с номером {phone}! Ваше сообщение получено.")
    return render(request, 'contacts.html')