from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    tags = models.ManyToManyField('Tag', related_name='posts')

class Tag(models.Model):
    name = models.CharField(max_length=100)