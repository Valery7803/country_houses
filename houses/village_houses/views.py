from django.shortcuts import render
from django.http import HttpResponse


# Функция главной страницы
def index(request):
    return render(request,'village_houses/index.html')


# Функция страницы про нас
def about(request):
    return render(request, 'village_houses/about.html')


# Функция страницы контакты
def contacts(request):
    return render(request,'village_houses/contacts.html')


# Функция обзора выбранного дома
def show_house(request, home_id):
    return HttpResponse('Ваш дом {home_id}')