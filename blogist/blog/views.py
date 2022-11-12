from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.conf import settings

def index(request):
    ctx = {}
    articles = Article.objects.filter(status=1)
    ctx['title'] = 'Home'
    ctx['articles'] = articles
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
        # print("Form data")
        # print(article_form.cleaned_data)
        article = article_form.save(commit=False) # save the form partially
        article.author = request.user 
        article.save()
        messages.success(request, 'Article created successfully')  

    ctx['article_form'] = article_form
    ctx['category_form'] = category_form
    ctx['tag_form'] = tag_form
    ctx['image_form'] = image_form
    return render(request, 'blog/create.html', ctx)

# ajax base views
def category_create(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            cat = category_form.save(commit=False)
            cat.save()
            return JsonResponse({'status': 'success', 'name': cat.name, 'id': cat.id})
        else:
            return JsonResponse({'status': 'invalid data'})
    else:
        return JsonResponse({'status': 'error'})

def tag_create(request):
    if request.method == 'POST':
        tag_form = TagForm(request.POST)
        if tag_form.is_valid():
            tag = tag_form.save(commit=False)
            tag.save()
            return JsonResponse({'status': 'success', 'name': tag.name, 'id': tag.id})
        else:
            return JsonResponse({'status': 'invalid data'})
    else:
        return JsonResponse({'status': 'error'})

def image_upload(request):
    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        print(image_form)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.save()
            return JsonResponse({'status': 'success', 'name': image.image.name, 'id': image.id})
        else:
            return JsonResponse({'status': 'invalid data'})
    else:
        return JsonResponse({'status': 'error'})

def article_view(request, id):
    ctx = {}
    article = get_object_or_404(Article, id=id)
    ctx['title'] = article.title
    ctx['article'] = article
    return render(request, 'blog/detail.html', ctx)

def search_article(request):
    ctx = {}
    query = request.GET.get('q')
    # print(query)
    ctx['articles'] = Article.objects.filter(content__icontains=query).filter(status=1)
    ctx['q'] = query
    return render(request, 'blog/search.html',ctx)


