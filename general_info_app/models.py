from django.db import models

# Create your models here.


class Address(models.Model):
    company_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name



class Socialnetwork(models.Model):
    link = models.URLField(max_length=200)
    code = models.IntegerField()

    def __str__(self):
        return self.link


class Faqs(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

