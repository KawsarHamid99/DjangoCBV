from unicodedata import name
from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    roll=models.IntegerField()
    subject=models.CharField(max_length=100,blank=True,null=True)