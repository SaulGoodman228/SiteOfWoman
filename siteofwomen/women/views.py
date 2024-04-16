import os
import uuid

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView

from women.forms import AddPostForm, UploadFileForm
from women.models import Women, Category, TagPost, UploadFiles

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

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Главная страница',
            'menu': menu,
            'cat_selected': 0,
            }
    # Метод для класса ListView который будет возвращать отображаемый список
    def get_queryset(self):
        return Women.published.all().select_related('cat')

    # template_name = 'women/index.html'
    # extra_context = {'title': 'Главная страница',
    #         'menu': menu,
    #         'posts': Women.published.all().select_related('cat'),
    #         'cat_selected': 0,
    #         }

    # def get_context_data(self, **kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context['title'] = 'Главная страница'
    #     context['menu'] = menu
    #     context['posts'] = Women.published.all().select_related('cat')
    #     context['cat_selected'] = int(self.request.GET.get('cat_id',0))
    #     return context


# def handle_uploaded_file(f):
#     # Получаем расширение файла
#     _, extension = os.path.splitext(f.name)
#
#     # Генерируем уникальное имя файла с помощью uuid
#     unique_filename = str(uuid.uuid4()) + extension
#
#     with open(os.path.join("uploads", unique_filename), "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def about(request):
    if request.method == 'POST':

        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp=UploadFiles(file=form.cleaned_data['file'])
            fp.save()
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

class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        context['menu'] = menu
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])

def cautegories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")



class WomenCategory(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = 'Категория' + cat.name
        context['menu'] = menu
        context['cat_selected'] = cat.pk
        return context



def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')



class TagPostList(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag =TagPost.objects.get(slug=self.kwargs['tag_slug'])
        context['title'] = 'Тег' + tag.tag
        context['menu'] = menu
        context['cat_selected'] = None
        return context

    def get_queryset(self):
        return Women.published.filter(tags__slug=self.kwargs['tag_slug']).select_related()

def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # try:
            #     Women.objects.create(**form.cleaned_data)
            #     return redirect('home')
            # except:
            #     form.add_error(None, 'Error add post')
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    
    data = {
        'menu': menu,
        'title': 'Добавлеение статьи',
        'form': form
    }
    return render(request, "women/addpage.html", data)

class AddPage(CreateView):
    form_class = AddPostForm
    #fields = '__all__'
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'menu':menu,
        'title':'Добавление статьи'
    }

class UpdatePage(UpdateView):
    model = Women
    fields = ['title','content','photo','is_published','cat','tags']
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'menu': menu,
        'title': 'Реактирование статьи'
    }


# class AddPage(View):
#     def get(self, request):
#         form = AddPostForm()
#         data = {
#             'menu': menu,
#             'title': 'Добавлеение статьи',
#             'form': form
#         }
#         return render(request, "women/addpage.html", data)
#
#     def post(self, request):
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         data = {
#             'menu': menu,
#             'title': 'Добавлеение статьи',
#             'form': form
#         }
#         return render(request, "women/addpage.html", data)

def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")
