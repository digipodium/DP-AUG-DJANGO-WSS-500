from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add_product, name='product_add'),
    path('', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
