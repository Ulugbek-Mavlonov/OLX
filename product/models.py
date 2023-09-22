from django.db import models
from rest_framework import serializers, viewsets


class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    user = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class District(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    user = models.IntegerField()

    def __str__(self):
        return self.name