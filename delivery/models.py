from django.db import models

class Delivery(models.Model):
    class Meta:
        verbose_name_plural = "Deliveries"
    name = models.CharField(max_length = 32)
    address = models.CharField(max_length = 255)
    phoneNumber = models.CharField(max_length = 20)
    delivery_time = models.DateTimeField()
    is_delivered = models.BooleanField(default=False)
