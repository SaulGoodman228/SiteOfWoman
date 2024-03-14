from django.db import models
from django.urls import reverse


# Create your models here.


class Women(models.Model):
    title = models.CharField(max_length= 255)
    slug=models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add= True)
    time_update = models.DateTimeField(auto_now= True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    #Отвечает за отображение в опред Виде

    class Meta:
        ordering =['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]
        #Ordering - отвечает как по стандарту будет сортироваться дб
        #indexes - индексирует заданный нами параметр

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug':self.slug})