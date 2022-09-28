from django.db.models import *

class Movies(Model):
    title = CharField(max_length=50)
    year = IntegerField()
    rating = FloatField()

    def __str__(self):
        return self.title

class Show(Model):
    title = CharField(max_length=60)
    year = IntegerField()
    season_count = IntegerField()
    rating = FloatField()
    created_at = DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}({self.year})'

class Student(Model):
    name = CharField(max_length=50)
    klass = IntegerField(verbose_name='class')
    rollno = IntegerField(verbose_name='roll number')

    def __str__(self):
        return self.name

class Report(Model):
    english = IntegerField()
    maths = IntegerField()
    science = IntegerField()
    hindi = IntegerField()
    socialscience = IntegerField()
    computer = IntegerField()
    student = ForeignKey('Student', on_delete=DO_NOTHING)

    def __str__(self) -> str:
        return f'Report of {self.student.name}'

class Weather(Model):
    temp = DecimalField(verbose_name="Temp(C)", max_digits=5, decimal_places=2)
    wind_speed = DecimalField(max_digits=5, decimal_places=2)
    humidity = DecimalField(max_digits=5, decimal_places=2)
    date = DateField(auto_now_add=True)

    def __str__(self):
        return self.temp

# python manage.py makemigrations
# python manage.py migrate



