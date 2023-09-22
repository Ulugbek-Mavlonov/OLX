from django.db import models

from rest_framework import serializers, viewsets



from account.models import CustomUser
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='images')
    status = models.BooleanField(default=True)
    parent = models.ForeignKey('self', blank=True, related_name='childs', on_delete=models.PROTECT)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='custom')

    class Meta:
        ordering = ['name',]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
>>>>>>> bf8a4b6a47896497632f5b08c313d1263e22f242
    

    
<<<<<<< HEAD




class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category')
    description = models.TextField()
    image = models.ImageField()
    location = models.IntegerField()
    price = models.IntegerField()
    views_count = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='customuser')
    is_active = models.BooleanField()
    is_banned = models.BooleanField()
    created_at= models.TimeField(auto_created=True)
    updated_at = models.TimeField(auto_now_add=True)
    is_deleted = models.BooleanField()
    
    class Meta:
        ordering = ['name',]
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    
>>>>>>> bf8a4b6a47896497632f5b08c313d1263e22f242

    
    
class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    user = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class District(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    user = models.IntegerField()
    def __str__(self):
        return self.name