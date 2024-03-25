from django.db import models
from django.utils import timezone

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=100)

class Purchased(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchasedDate = models.DateTimeField(default=timezone.now,null=True,blank=False)
