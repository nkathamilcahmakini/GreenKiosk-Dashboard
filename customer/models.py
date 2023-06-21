from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    purchase_product = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    total_price = models.FloatField()
    mode_of_payment = models.CharField(max_length=255)

