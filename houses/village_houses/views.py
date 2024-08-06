from django.shortcuts import render
from django.http import HttpResponse

menu = [
    {'title':'Страница про нас', 'url_name':'about'},
    {'title':'Наши контакты', 'url_name':'contacts'},
]

# Функция главной страницы
def index(request):
    data = {'title':'Главная страница','menu': menu}
    return render(request,'village_houses/index.html', data)


# Функция страницы про нас
def about(request):
    data = {'title':'Страница про нас', 'menu': menu}
    return render(request, 'village_houses/about.html', data)


# Функция страницы контакты
def contacts(request):
    data = {'title':'Наши контакты', 'menu': menu}
    return render(request,'village_houses/contacts.html', data)


# Функция обзора выбранного дома
def show_house(request, home_id):
    return HttpResponse(f'Ваш дом <p>id:{home_id}</p>')