# Generated by Django 4.2.1 on 2024-04-11 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0010_uploadfiles_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
