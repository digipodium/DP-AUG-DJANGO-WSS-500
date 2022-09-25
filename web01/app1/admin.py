from django.contrib import admin
from .models import Movies, Show

admin.site.register(Movies) # this line add ur table to admin dashboard
admin.site.register(Show)