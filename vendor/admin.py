from django.contrib import admin
from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ("vendor_name","shop_name","phone_number")
admin.site.register(Vendor,VendorAdmin)
