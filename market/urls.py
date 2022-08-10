from rest_framework.routers import DefaultRouter
from market.views import AuthorAPIView, GenreAPIView, BookListAPIView

router = DefaultRouter()

#Регистрация вьюшек
router.register(r'book', BookListAPIView, basename='book')
router.register(r'author', AuthorAPIView, basename='author')
router.register(r'genre', GenreAPIView, basename='genre')

urlpatterns = []

urlpatterns += router.urls
