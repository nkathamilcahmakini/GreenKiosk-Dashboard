from django.db import models
from inventory.models import Product

class Cart(models.Model):
    product = models.ManyToManyField(Product)
    product_name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    image = models.ImageField()
    price = models.IntegerField()
    date = models.DateTimeField()

