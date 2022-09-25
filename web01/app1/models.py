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





