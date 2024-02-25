from django.urls import path

from women import views



urlpatterns = [
    path('women/',views.index),        #http://127.0.0.1:8000/women/
    path('cats/<slug:cat_slug>/',views.cautegories_by_slug),     #http://127.0.0.1:8000/cats/
]

