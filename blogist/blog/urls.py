from django.urls import path
from .views import *

urlpatterns = [
    path('', landing, name='landing'),
    path('home/', index, name='home'),
]