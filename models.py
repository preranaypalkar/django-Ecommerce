from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    address = models.CharField(max_length=10)




class Product(models.Model):
    id=models.AutoField(primary_key=True)
    shape = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    price = models.CharField(max_length=10)