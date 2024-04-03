from django.contrib import admin
from .models import Women, Category

# Register your models here.

admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Известные женщины мира'

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    #отображение нужных полей
    list_display = ('id','title','time_create','is_published','cat')

    #кликабельность поля
    list_display_links = ('id',)

    #указание сортировки полей только для админ панели
    ordering = ['time_create','title']

    list_editable = ('is_published','title','cat')

    list_per_page = 5

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


#admin.site.register(Women, WomenAdmin)