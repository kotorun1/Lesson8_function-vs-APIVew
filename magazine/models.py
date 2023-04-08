from django.db import models
from customauth.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    country_manufacturer = models.CharField(max_length=100)
    category = models.ManyToManyField(Category,blank = True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return "Корзина " + self.user.username


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    full_cost = models.IntegerField()

    def __str__(self):
        return str(self.full_cost)
