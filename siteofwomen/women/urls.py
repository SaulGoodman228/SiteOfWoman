from django.urls import path, register_converter
from . import converters
from women import views

register_converter(converters.FourDigitYearConverter,"year4")

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('addpage/',views.add_page,name='add_page'),
    path('post/<slug:post_id>', views.show_post, name='post'),
    path('category/<int:cat_id>/',views.show_category,name='category'),
]

