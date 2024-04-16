from django.urls import path, register_converter
from . import converters
from women import views

register_converter(converters.FourDigitYearConverter,"year4")

urlpatterns = [
    path('',views.WomenHome.as_view(),name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('addpage/',views.AddPage.as_view(),name='add_page'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/',views.WomenCategory.as_view(),name='category'),
    path('tag/<slug:tag_slug>/',views.TagPostList.as_view(),name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
]

