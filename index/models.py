from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class kurser(models.Model):
    titel = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    tekst = RichTextField(blank=True, null=True)
    billede = models.ImageField(upload_to='uploads/', blank=True, null=True)


class om(models.Model):
    titel = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    tekst = RichTextField(blank=True, null=True)
    billede = models.ImageField(upload_to='uploads/', blank=True, null=True)


class about(models.Model):
    tekst = RichTextField(blank=True, null=True)


class plakater(models.Model):
    titel = models.CharField(max_length=100)
    billede = models.ImageField(upload_to='uploads/', blank=True, null=True)


class books(models.Model):
    titel = models.CharField(max_length=100)
    tekst = RichTextField(blank=True, null=True)
    billede = models.ImageField(upload_to='uploads/', blank=True, null=True)
    forlag = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
