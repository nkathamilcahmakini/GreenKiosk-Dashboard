from django.db import models
from vendor.models import Vendor

class Product (models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add = True)
    date_appdated = models.DateTimeField(auto_now = True)
    stock = models.PositiveIntegerField()
    Vendor = models.ForeignKey(Vendor, null=True, on_delete=models.CASCADE)

 
  