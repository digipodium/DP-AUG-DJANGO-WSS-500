from django.urls import path
from .views import *

urlpatterns = [
    path('', OrderSummaryView.as_view(), name='order_summary'),
    path('item/add/<slug>/', OrderItemAddView.as_view(), name='add_to_cart'),
    path('item/remove/<slug>/', OrderItemDeleteView.as_view(), name='remove_from_cart'),
]
