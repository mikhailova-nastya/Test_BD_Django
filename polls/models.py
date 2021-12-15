from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Product(models.Model):
    item = models.CharField(max_length=50) # product name
    description = models.TextField(blank=False)
    category = models.ForeignKey(Category, blank = True, null = True, on_delete = models.CASCADE) #product category
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.item



class Customer(models.Model):
    email=models.EmailField(max_length=254)
    buyer_name=models.CharField(max_length=50)

    def __str__(self):
        return self.buyer_name

class Discount(models.Model):
    disc_value=models.IntegerField(default=0)
    disc_title=models.CharField(max_length=50)
    category = models.ForeignKey(Category, blank = True, null = True, on_delete = models.DO_NOTHING) #product category

    def __str__(self):
        return self.disc_title


import datetime
from django.utils import timezone


class Sell(models.Model):
    customer = models.ForeignKey(Customer, blank = True, null = True, on_delete = models.DO_NOTHING)
    time_of_purchase=models.DateTimeField('date of purchase')
    product = models.ForeignKey(Product, blank = True, null = True, on_delete = models.DO_NOTHING)
    amount_of_items=models.IntegerField(default=1) #amount of sold items
    disc =  models.ForeignKey(Discount, blank = True, null = True, on_delete = models.DO_NOTHING)








