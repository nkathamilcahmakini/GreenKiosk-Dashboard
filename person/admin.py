from django.contrib import admin
from .models import Person

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "password", "phonenumber", "address")
admin.site.register(Person, PersonAdmin)
