from django.db import models

from profiles.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  
    ptype = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.FloatField()