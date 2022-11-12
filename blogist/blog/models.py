from django.db import models
from django.conf import settings
# pip install `django-tinymce` for the import below
from tinymce.models import HTMLField

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='articles/images/')
    caption = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.image.url

class Article(models.Model):

    class StatusChoice(models.IntegerChoices):
        DRAFT = 0, 'Draft'
        PUBLISHED = 1, 'Published'
    
    title = models.CharField(max_length=100, unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(choices=StatusChoice.choices, default=StatusChoice.DRAFT)
    tags = models.ManyToManyField(Tag)
    duration = models.DurationField()
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.author}'