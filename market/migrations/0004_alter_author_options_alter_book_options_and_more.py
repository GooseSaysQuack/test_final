# Generated by Django 4.0.6 on 2022-08-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_book_genre_book_oblojka'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
