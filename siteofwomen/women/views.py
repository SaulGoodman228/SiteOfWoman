import os
import uuid

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string

from women.forms import AddPostForm, UploadFileForm
from women.models import Women, Category, TagPost

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):  # HttpRequest

    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': Women.published.all().select_related('cat'),
            'cat_selected': 0,
            }
    return render(request, 'women/index.html', data)


def handle_uploaded_file(f):
    # Получаем расширение файла
    _, extension = os.path.splitext(f.name)

    # Генерируем уникальное имя файла с помощью uuid
    unique_filename = str(uuid.uuid4()) + extension

    with open(os.path.join("uploads", unique_filename), "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def about(request):
    if request.method == 'POST':

        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
    else:
        form = UploadFileForm()

    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu, 'form':form})


def cautegories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")


def archive(request, year):
    if 1990 <= int(year) <= 2023:
        return HttpResponse(f'<h1>Архив за Год: {year}</h1>')
    else:
        return redirect('home', permanent=True)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {'title': post.title,
            'menu': menu,
            'post': post,
            'cat_selected': 1}
    return render(request, 'women/post.html', data)


def cautegories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')
    data = {'title': f'Рубрика {category.name}',
            'menu': menu,
            'posts': posts,
            'cat_selected': category.pk,
            }
    return render(request, 'women/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')


def show_tag_postlist(request, tag_slug):


    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related('cat')
    data = {
        'title': f'Tag: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None
    }
    return render(request, 'women/index.html', context=data)


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # try:
            #     Women.objects.create(**form.cleaned_data)
            #     return redirect('home')
            # except:
            #     form.add_error(None, 'Error add post')
            form.save()
    else:
        form = AddPostForm()
    
    data = {
        'menu': menu,
        'title': 'Добавлеение статьи',
        'form': form
    }
    return render(request, "women/addpage.html", data)

def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")
