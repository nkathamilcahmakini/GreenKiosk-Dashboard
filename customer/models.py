from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    firstname = models.CharField(max_length= 32)
    lastname = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=55)
    phonenumber = models.CharField(max_length=20)
    address = models.CharField(max_length=55)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

