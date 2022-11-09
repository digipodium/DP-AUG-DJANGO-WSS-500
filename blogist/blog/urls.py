from django.urls import path
from .views import *

urlpatterns = [
    path('', landing, name='landing'),
    path('home/', index, name='home'),
    path('article/new/', article_create, name='create'),
    path('api/category/create/', category_create, name='cat_create'),
    path('api/tag/create/', tag_create, name='tag_create'),
    path('article/<int:id>/view/', article_view, name='view'),
]