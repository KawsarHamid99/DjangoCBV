from email.policy import default
from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(null=True)
    author=models.CharField(max_length=100)
    isbn=models.CharField(max_length=100)
    count=models.IntegerField(null=True,default=0)