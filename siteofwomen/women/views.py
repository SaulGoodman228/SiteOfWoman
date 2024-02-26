from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

# Create your views here.
def index(request): #HttpRequest
    return HttpResponse("Леди Гага")

def cautegories(request,cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def archive(request,year):
    if 1990 <= int(year) <= 2023:
        return HttpResponse(f'<h1>Год: {year}</h1>')
    else:
        return Http404('IdiNahuy')


def cautegories_by_slug(request,cat_slug):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")

def page_not_found(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
