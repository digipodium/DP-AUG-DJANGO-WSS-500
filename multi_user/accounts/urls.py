from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_login, name='select_login'),
    path('student/login/', views.student_login, name='student_login'),
    path('student/register/', views.student_register, name='student_register'),
    path('student/home/', views.student_home, name='student_home'),
    # path('company/login/', views.company_login, name='company_login'),
    # path('company/register/', views.company_register, name='company_register'),
    # path('company/home/', views.company_home, name='company_home'),
]