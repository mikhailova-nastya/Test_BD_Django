from django.db import models
import datetime
from django.utils import timezone
from decimal import Decimal


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(max_length=50)  # product name
    description = models.TextField(blank=False)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)  # product category
    price = models.DecimalField(max_digits=6, decimal_places=0, default=0)

    def __str__(self):
        return self.name


class Customer(models.Model):
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Discount(models.Model):
    value = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.DO_NOTHING)  # product category

    def __str__(self):
        return self.title


class Sell(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.DO_NOTHING)
    time_of_purchase = models.DateTimeField('date of purchase')
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.DO_NOTHING)
    amount_of_items = models.IntegerField(default=1)  # amount of sold items
    discount = models.ForeignKey(Discount, blank=True, null=True, on_delete=models.DO_NOTHING)
