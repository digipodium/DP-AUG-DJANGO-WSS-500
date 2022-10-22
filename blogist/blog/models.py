from enum import unique
from tabnanny import verbose
from django.db import models
from django.conf import settings
from tinymce.models import HTMLField

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



