# Generated by Django 4.0.3 on 2022-04-06 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_post_post_category_alter_post_rating_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
    ]
