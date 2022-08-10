from rest_framework import serializers
from market.models import (
    Book, Author, Genre
)

#Сериализатор книг
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'title', 'authors',
                  'publication_date', 'genre', 'oblojka')


#Сериализатор авторов
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')


#Сериализатор жанров
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')
