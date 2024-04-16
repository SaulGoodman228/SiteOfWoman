from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Husband, RussianValidator, Women


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = ['title', 'slug','photo', 'content', 'is_published', 'cat', 'husband', 'tags']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':50,'rows':5}),
        }
        labels = {'slug':'URL'}

    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбранна',
                                  label='Категория')

    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label='Не замужем', label='Муж',
                                     required=False)

    # Проверка для поля title (clean_названиие-поля)
    # def clean_title(self):
    #     title=self.cleaned_data['tite']
    #     ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- '
    #
    #     if not (set(title) <= set(self.ALLOWED_CHARS)):
    #         raise ValidationError(self.message,code=self.code)
    #     return title

class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')