from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from market.models import Author, Book, Genre
from market.serializers import BookSerializer, AuthorSerializer, GenreSerializer


class BookListAPIView(APIView):

    def get(self, request):
        book_qs = Book.objects.all()
        serializer = BookSerializer(instance=book_qs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class AuthorAPIView(APIView):
    def get(self, request):
        author_qs = Author.objects.all()
        serializer = AuthorSerializer(instance=author_qs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class GenreAPIView(APIView):
    def get(self, request):
        genre_qs = Genre.objects.all()
        serializer = GenreSerializer(instance=genre_qs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    