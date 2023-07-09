from django.db import models

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50)
    shop_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=32)

