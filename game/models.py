from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Royal(models.Model):
    name=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True)


class Family(models.Model):
    royal=models.ForeignKey(Royal, on_delete=models.PROTECT) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True)
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100, unique=True)
    summary=RichTextField()
    description=RichTextField()
    photo=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)


class Page(models.Model):
    title=models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=255, unique=True)
    content=RichTextField()
    image=models.ImageField(upload_to='page/%y/%m/%d/', blank=True)


class Popular(models.Model):
    title=models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=250, unique=True)
    content=RichTextField()
    image=models.ImageField(upload_to='page/%y/%m/%d/', blank=True)

        


