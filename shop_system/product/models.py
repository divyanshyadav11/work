from django.db import models

from profiles.models import User


class Category(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'media',default='home/ubox79/Downloads/logo.jpg')
    description = models.CharField(max_length=500)
        

    def __str__(self):
    	return self.category

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'media',default='home/ubox79/Downloads/logo.jpg',unique=False) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    price = models.FloatField()

