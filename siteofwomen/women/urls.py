from django.urls import path, register_converter
from . import converters
from women import views

register_converter(converters.FourDigitYearConverter,"year4")

urlpatterns = [
    path('',views.main_paige,name='home'),
    path('about/',views.about, name='about'),
    path('women/',views.index,name='women'),        #http://127.0.0.1:8000/women/
    path('archive/<year4:year>/',views.archive,name='archive_year'),
    path('cats/<slug:cat_slug>/',views.cautegories_by_slug,name='cats_slug'),     #http://127.0.0.1:8000/cats/

]

