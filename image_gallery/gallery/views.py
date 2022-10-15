from django.shortcuts import render, redirect
from .models import Category, Image # (important) get the class of Category & Image
from .forms import CategoryForm, ImageForm
import os

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
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cat = Category(name=name)
            cat.save()
            return redirect('index')
    ctx = {
        'form': form,
        'title' : 'Add Category',
    }
    return render(request, 'add_category.html', ctx)

def add_image(request):
    form = ImageForm() # create an empty form object
    
    if request.method == 'POST':                        # if the form is submitted
        form = ImageForm(request.POST, request.FILES)   # create a form object with data
        if form.is_valid():                             # check if the form is valid
            title = form.cleaned_data['title']          # get the title from the form
            category = form.cleaned_data['category']    # get the category from the form
            image = form.cleaned_data['image']          # get the image from the form
            img = Image(title=title, category=category, image=image) # create an image object
            img.save()                                  # save the image object to database
            return redirect('index')                              
    ctx = {
        'form': form,
        'title' : 'Add/Upload Image',
    }
    return render(request, 'add_image.html', ctx)

def view_image(request, image_id):
    try:
        item = Image.objects.get(id=image_id)   # get the image using the id
        ctx = {
            'img': item,
            'title' : item.title,
        }
        return render(request, 'image_view.html', ctx)
    except:
        return redirect('index')

def delete_image(request, image_id):
    try:
        item = Image.objects.get(id=image_id)   # get the image using the id
        os.remove(item.image.path)              # delete the image file from media folder
        item.delete()                           # delete the image from database
    except:
        print('Error deleting image')
    return redirect('index')