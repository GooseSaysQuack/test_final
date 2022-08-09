"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from http import server
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from market.views import AuthorAPIView, BookListAPIView, GenreAPIView
from .yasg import urlpatterns as doc_urls
from . import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/books/', BookListAPIView.as_view(), name='books-url'),
    path('api/v1/authors/', AuthorAPIView.as_view(), name='authors-url'),
    path('api/v1/genres/', GenreAPIView.as_view(), name='genres-url'),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include ('djoser.urls.authtoken')),
]

scheme_view = get_swagger_view(title='Pastebin API')

urlpatterns += router.urls, doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += re_path(r'^media/(?P<path>.*)$', server, {'document_root': settings.MEDIA_ROOT}),