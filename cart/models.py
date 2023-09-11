from django.db import models
from inventory.models import Product

class Cart(models.Model):
    product = models.ManyToManyField(Product)
    product_name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    image = models.ImageField()
    price = models.IntegerField()
    date = models.DateTimeField()

    def add_product(self, product):
        self.products.add(product)
        self.save()
        return self
    
    def get_total(self):
        products = self.products
        total = 0
        for product in products:
            total += product.price
        return total    