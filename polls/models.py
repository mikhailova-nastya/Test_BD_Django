from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Product(models.Model):
    item = models.CharField(max_length=50) # product name - а почему бы не назвать не item, а name ?
    description = models.TextField(blank=False)
    category = models.ForeignKey(Category, blank = True, null = True, on_delete = models.CASCADE) #product category
    price = models.IntegerField(default=0)  # Сумма в копейках? В какой валюте? В финтехе важно, знать про тип данных Decimal и чем он отличается от Float


    def __str__(self):
        return self.item



class Customer(models.Model):
    email=models.EmailField(max_length=254)  
    buyer_name=models.CharField(max_length=50)  # Вопросы нейминга, чем понятие buyer отличается от customer?

    def __str__(self):
        return self.buyer_name

class Discount(models.Model):
    disc_value=models.IntegerField(default=0)  # Кажется префикс disc_* не несет смысла - мы и так знаем, что это Discount
    disc_title=models.CharField(max_length=50)
    category = models.ForeignKey(Category, blank = True, null = True, on_delete = models.DO_NOTHING) #product category

    def __str__(self):
        return self.disc_title

# Все импорты должны размещаться в начале проекта, см PEP8
import datetime
from django.utils import timezone


class Sell(models.Model):
    customer = models.ForeignKey(Customer, blank = True, null = True, on_delete = models.DO_NOTHING)
    time_of_purchase=models.DateTimeField('date of purchase')  # Если все и так на английском, то хороший тон использовать i118n от Django
    product = models.ForeignKey(Product, blank = True, null = True, on_delete = models.DO_NOTHING)
    amount_of_items=models.IntegerField(default=1) #amount of sold items
    disc =  models.ForeignKey(Discount, blank = True, null = True, on_delete = models.DO_NOTHING)  # Мои личные предпочтения в нейминге - полные имена, т.е. disc => discount - тогда не нужно запоминать, какое именно сокращение мы придумали








