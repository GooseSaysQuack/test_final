from distutils.command.upload import upload
from django.db import models


# Модель автора
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


# Модель жанра
class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


# Модель книги
class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    title = models.CharField(max_length=1000)
    authors = models.ManyToManyField(Author)
    publication_date = models.CharField(max_length=15)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    oblojka = models.ImageField(
        upload_to='internet_shop/shop/media/',
        null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.price} {self.title} {self.authors} {self.publication_date} {self.genre} {self.oblojka}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
