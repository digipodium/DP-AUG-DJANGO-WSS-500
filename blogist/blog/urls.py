from django.urls import path
from .views import *

urlpatterns = [
    path('', landing, name='landing'),
    path('home/', index, name='home'),
    path('api/category/create/', category_create, name='cat_create'),
    path('api/tag/create/', tag_create, name='tag_create'),
    path('api/image/upload/', image_upload, name='image_create'),
    path('article/new/', article_create, name='create'),
    path('article/<int:id>/view/', article_view, name='view'),
    path('article/search/', search_article, name='search'),
]