from rest_framework.routers import DefaultRouter

from market.views import AuthorAPIView, GenreAPIView, BookListAPIView
from market.models import Book

router = DefaultRouter()

# router.register('book', BookViewSet)
router.register(r'book', BookListAPIView, basename='book')
router.register(r'author', AuthorAPIView, basename='author')
router.register('genre', GenreAPIView, basename='genre')

urlpatterns = []

urlpatterns += router.urls
