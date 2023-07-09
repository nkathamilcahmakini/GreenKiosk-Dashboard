from django.db import models

class Products(models.Model):
    class Meta:
        verbose_name_plural = "products"
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places = 2)
    description = models.TextField()
    image = models.ImageField()
    available_stock = models.PositiveIntegerField()
   
    