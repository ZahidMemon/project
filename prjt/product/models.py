from django.db import models

# Create your models here.

class Product(models.Model):
    productname=models.CharField(max_length=100)
    price=models.FloatField()
    quantity=models.IntegerField()