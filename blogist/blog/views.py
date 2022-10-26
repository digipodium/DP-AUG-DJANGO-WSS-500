from django.shortcuts import render

def index(request):
    ctx = {}
    
    ctx['title'] = 'Home'
    
    return render(request, 'blog/index.html', ctx)

def landing(request):
    ctx = {}
    ctx['title'] = 'Welcome to Blogist'
    return render(request, 'blog/landing.html', ctx)