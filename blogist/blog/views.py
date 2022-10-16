from django.shortcuts import render

def index(request):
    ctx = {}
    
    ctx['title'] = 'Home'
    return render(request, 'blog/index.html', ctx)