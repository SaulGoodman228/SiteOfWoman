from django.urls import path, register_converter
from . import converters
from women import views

register_converter(converters.FourDigitYearConverter,"year4")

urlpatterns = [
    path('women/',views.index),        #http://127.0.0.1:8000/women/
    path('cats/<year4:year>',views.archive),
    path('cats/<slug:cat_slug>/',views.cautegories_by_slug),     #http://127.0.0.1:8000/cats/

]

