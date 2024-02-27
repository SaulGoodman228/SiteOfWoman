from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

menu=['О сайте','Добавить статью','Обратная связь','Войти']

data_db = [ {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
            {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
            {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True}, ]

def main_paige(request):

    data={'title':'Главная страница',
          'menu':menu,
        'posts':data_db,
          }
    return render(request,'women/index.html',data)

def index(request): #HttpRequest
    return HttpResponse("Леди Гага")
def about(request):
    return render(request,'women/about.html',{'title':'О сайте'})

def cautegories(request,cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def archive(request,year):
    if 1990 <= int(year) <= 2023:
        return HttpResponse(f'<h1>Архив за Год: {year}</h1>')
    else:
        return redirect('home',permanent=True)


def cautegories_by_slug(request,cat_slug):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")

def page_not_found(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
