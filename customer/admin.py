from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "password", "phonenumber", "address")
admin.site.register(Customer, CustomerAdmin)
   
