from django.contrib import admin
from .models import Customer
# Register your models here.




@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'purchase_product', 'price', 'quantity', 'total_price', 'mode_of_payment')
admin.site.register(Customer, CustomerAdmin)    
