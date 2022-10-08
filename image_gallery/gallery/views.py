from django.shortcuts import render
from .models import Category, Image # (important) get the class of Category & Image

def index(request):
    categories = Category.objects.all() # get all the categories
    images = Image.objects.all()        # get all the images
    ctx = {
        'categories': categories,
        'images': images,
        'title' : 'Image Gallery',
    }
    return render(request, 'index.html', ctx)

def add_category(request):
    pass

def add_image(request):
    pass

def view_image(request,image_id):
    pass

def delete_image(request,image_id):
    pass