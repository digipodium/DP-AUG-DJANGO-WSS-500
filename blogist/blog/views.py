from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.conf import settings

def index(request):
    ctx = {}
    ctx['title'] = 'Home'
    return render(request, 'blog/index.html', ctx)

def landing(request):
    ctx = {}
    ctx['title'] = 'Welcome to Blogist'
    return render(request, 'blog/landing.html', ctx)

def article_create(request):
    ctx = {'title': 'Create Article | Blogist'}
    article_form = ArticleForm(request.POST or None)
    category_form = CategoryForm()
    tag_form = TagForm()
    image_form = ImageForm()
    if article_form.is_valid():
        pass
    ctx['article_form'] = article_form
    ctx['category_form'] = category_form
    ctx['tag_form'] = tag_form
    ctx['image_form'] = image_form
    return render(request, 'blog/create.html', ctx)

# ajax base views
def category_create(request):
    pass

def tag_create(request):
    pass

def image_upload(request):
    pass