from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        uname = form.cleaned_data.get('username')
        pwd = form.cleaned_data.get('password')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect ('/')
        else:
            messages.error(request, 'Wrong Credentials')
    ctx = {'form': form, 'title': 'Login|Blogist'}
    return render(request, "accounts/login.html", ctx)