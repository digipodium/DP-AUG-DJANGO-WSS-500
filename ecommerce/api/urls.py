from django.urls import path
from .views import get_product_list

urlpatterns = [
    path('products/',get_product_list, name='api_gpl'),
]