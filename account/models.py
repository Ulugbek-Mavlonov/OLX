from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=14)
    image = models.ImageField()
    custom_id = models.CharField(max_length=14, blank=True)
    role = models.CharField(max_length=50)
    # following = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profile')
    about = models.ImageField(upload_to='images/%Y/%m/%d/')
    birth_date = models.DateField(blank=True)
    skills = models.CharField(max_length=200)
    overview = models.CharField(max_length=200)
    