import imp
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from market.models import Author, Book, Genre
from market.serializers import BookSerializer, AuthorSerializer, GenreSerializer


# class BookViewSet(ReadOnlyModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


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

# class AuthorViewSet(ReadOnlyModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


# class GenreViewSet(ReadOnlyModelViewSet):
#     queryset = Genre.objects.all()
#     serializer_class = AuthorSerializer
