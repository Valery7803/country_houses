from django.shortcuts import render
from django.http import HttpResponse

# Имитируем базу данных в учебных целях
data_db = [
    {'id':1, 'title':'Дом "Мечта"', 'context':'Деревянный дом из строгоного бруса 150м2, одноэтажные коттеджи в стиле барнхаус: открытые планировки, панорамные окна и большая терраса.'},
    {'id':2, 'title':'Дом "Ривьера"', 'context':'Деревянный дом из оцилиндрованного бруса 200м2, Премиальные двухэтажные коттеджи «Ривьера»: панорамные окна, просторная терраса и два отдельных входа.'},
    {'id':3, 'title':'Дом "Акварель"', 'context':'Деревянный дом щитовой 185м2, Одноэтажные коттеджи «Акварель» с перголой, вторым светом и панорамными окнами позволяют любоваться природой, не выходя из дома.'},
]

menu = [
    {'title':'Страница про нас', 'url_name':'about'},
    {'title':'Наши контакты', 'url_name':'contacts'},
]

# Функция главной страницы
def index(request):
    data = {
        'title':'Главная страница',
        'menu': menu,
        'home': data_db,
    }
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