from django.contrib import admin
from .models import Promotion

class PromotionAdmin(admin.ModelAdmin):
    list_display = ("product_name","description","discount","start_date","end_date")
admin.site.register (Promotion,PromotionAdmin)

