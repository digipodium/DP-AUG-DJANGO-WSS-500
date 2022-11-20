from django.db import models
from django.contrib.auth.models import User



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    course = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    passing_year = models.IntegerField()

    def __str__(self):
        return self.user.email
    

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=10)
    company_email = models.EmailField(unique=True)
    company_website = models.CharField(max_length=100)
    company_description = models.TextField()
    # company_logo = models.ImageField(upload_to='company_logo', blank=True)

    def __str__(self):
        return self.user.email
