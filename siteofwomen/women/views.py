from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

menu=['О сайте','Добавить статью','Обратная связь','Войти']

class MyClass:
    def __init__(self,v1,v2):
        self.a=v1
        self.b=v2


def main_paige(request):
    # t=render_to_string('women/index.html')
    # return HttpResponse(t)
    data={'title':'Главная страница',
          'menu':menu,
          'float':28.56,
          'lst':[1,2,'abc',True],
          'set':{1,2,3,4,5},
          'dict':{'key_1':'value_1','key_2':'value_2'},
          'obj':MyClass(10,20),
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
