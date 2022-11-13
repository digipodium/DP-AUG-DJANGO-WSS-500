from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('logout/', logout_view, name='logout'),
    path('profile/', login_required(ProfileView.as_view()), name='profile'),
    path('contact/', ContactView.as_view(), name='contact'),
]
