from django.shortcuts import render
# import login
from django.contrib.auth import login,  authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Company

def select_login(request):
    return render(request, 'select_login.html')

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['is_student'] = True
            return redirect('student_home')
        else:
            return render(request, 'student_login.html', {'error': 'Invalid Credentials'})
    else:
        return render(request, 'student_login.html')    

def student_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        course = request.POST['course']
        stream = request.POST['stream']
        roll_no = request.POST['roll_no']
        phone = request.POST['phone']
        city = request.POST['city']
        passing_year = request.POST['passing_year']
        # first create a new user
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return render(request, 'student_register.html' )
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return render(request, 'student_register.html' )
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                student = Student(user=user, course=course, stream=stream, roll_no=roll_no, phone=phone, city=city, passing_year=passing_year)
                student.save()
                messages.success(request, 'Student Registration Successful')
                return redirect('student_login')
        else:
            messages.error(request, 'Passwords do not match')
            return render(request, 'student_register.html' )
    return render(request, 'student_register.html')

def student_home(request):
    companies = Company.objects.all()
    ctx = {'companies': companies}
    return render(request, 'student_home.html', ctx)

def company_login(request):
    return render(request, 'company_login.html')

def company_register(request):
    return render(request, 'company_register.html')

def company_home(request):
    return render(request, 'company_home.html')



    