from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Women, Category

# Register your models here.

admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Известные женщины мира'

#Создание пользовательского фильтра
class MarriedFilter(admin.SimpleListFilter):
    title = 'Status'
    parameter_name = 'status'
    def lookups(self, request, model_admin):
        return[
            ('married','Замужняя'),
            ('single','Не замужняя'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)
        else:
            return queryset.all()

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    #отображение нужных полей
    list_display = ('title','post_photo','time_create','is_published','cat')
    list_display_links = ('title',)
    readonly_fields = ['post_photo']
    #указание сортировки полей только для админ панели
    ordering = ['time_create']
    list_editable = ('is_published','cat')
    list_per_page = 10
    #Добавление пользовательских действий в список
    actions=('set_published','set_draft')
    #позволяет проводить поиск по выбранным полям
    search_fields = ['title','cat__name']
    #Добавление полей фильтрации
    list_filter = [MarriedFilter,'cat__name','is_published']
    #поля отоброжаемые в форме для редактирования
    fields = ['title','content','photo','post_photo','slug','cat','husband']
    # exclude делает то же только наоборот readonly_fields - делает поля нередактируемыми

    #автоматически транслитирует поле по другому полю
    prepopulated_fields = {'slug':('title',)}

    #filter_horizontal = ['tags']




    #Пользовательское поле
    @admin.display(description='Краткое описание',ordering='content')
    def brief_info(self, women: Women):
        return f'Описание {len(women.content)}'

    #Пользовательское действие
    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request,f'Измененно {count} записей')

    @admin.action(description='Снять с публикации выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'{count} записей снято с публикации!', messages.WARNING)

    @admin.display(description='Фото',ordering='content')
    def post_photo(self, women:Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}' width=50>")
        else:
            return 'без фото'
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


#admin.site.register(Women, WomenAdmin)