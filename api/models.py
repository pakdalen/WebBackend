from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=60)

class SubCategory(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

class Product(models.Model):
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    image = models.CharField(max_length=600)
    price = models.FloatField()
    quantity = models.IntegerField(default=12)

class Order(models.Model):
    user = models.CharField(max_length=500)
    phoneNumber = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
