from django.db import models

class Refunds(models.Model):
    class Meta:
        verbose_name_plural = "Refunds"
    order_number = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.order_number
