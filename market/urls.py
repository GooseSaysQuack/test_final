from rest_framework.routers import DefaultRouter

from market.views import AuthorAPIView, GenreAPIView, BookListAPIView

router = DefaultRouter()

# router.register('book', BookViewSet)
router.register('book', BookListAPIView)
router.register('author', AuthorAPIView)
router.register('genre', GenreAPIView)

urlpatterns = []

urlpatterns += router.urls
