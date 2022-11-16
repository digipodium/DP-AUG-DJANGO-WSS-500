from django.shortcuts import render
from .models import Game

def home(request):
    ctx = {
        'games': Game.objects.all()
    }
    return render(request, 'home.html', ctx)