from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Product(models.Model):

    title = models.CharField(max_length = 100)
    description = models.CharField(max_length=400)
    price = models.IntegerField(default = 0)
    stock = models.IntegerField(default = 0)
    timeOfcreation = models.DateTimeField(default = timezone.now)


    def __str__(self):
        return self.title

class User(models.Model):

    name = models.CharField(max_length = 100)
    description = models.CharField(max_length=400)


    def __str__(self):
        return self.name


class Cart(models.Model):

    productId = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', null=True, blank=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer', null=True, blank=True)
    timeOfAllocation = models.DateTimeField(default = timezone.now)
    noOfItemsOrdered = models.IntegerField(default = 0)
