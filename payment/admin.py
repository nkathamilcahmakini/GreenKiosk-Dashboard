from django.contrib import admin
from .models import Payment

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "amount", "payment_method", "payment_description", "payment_method_name")
admin.site.register(Payment, PaymentAdmin)
