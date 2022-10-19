from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

User = get_user_model() # get the user model

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
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

# register view
def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        if password1 == password2:
            user = User.objects.create_user(username, email, password1)
            user.save()
            messages.success(request, 'Registration Successful')
            return redirect('/') # redirect to home page
        else:
            messages.error(request, 'Passwords do not match!')
    ctx = {'form': form, 'title':'Register|Blogist'}
    return render(request, "accounts/register.html", ctx)
