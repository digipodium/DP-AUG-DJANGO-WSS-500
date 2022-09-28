from django.contrib import admin
from .models import Movies, Show, Student, Report, Weather

admin.site.register(Movies) # this line add ur table to admin dashboard
admin.site.register(Show)

# admiview to create admin template for models

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('rollno','klass','name')
    search_fields = ('name','klass')
    ordering = ('name',)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('student','english','hindi','maths','science',
        'socialscience','computer')

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('date','temp','humidity','wind_speed')
    list_filter = ('date',)
    ordering = ('date',)
