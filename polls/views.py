from django.shortcuts import render


from django.http import HttpResponse
from django.db.models import Min, Max

from .models import Product
from .models import Sell

from datetime import datetime

from django.utils import timezone

from django.shortcuts import render

import csv

#start page
def index(request):

    return render(request, 'polls/index.html')


#report N1

def report1(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Time', 'Item', 'Price', 'Discount', 'Discount Value'])

    for p in Sell.objects.filter(time_of_purchase__gt=datetime(2021, 12, 2), time_of_purchase__lt=datetime(2021, 12, 4)).values_list('time_of_purchase', 'product__item', 'product__price', 'disc__disc_title', 'disc__disc_value'):
        writer.writerow(p)

    response['Content-Disposition'] = 'attachment; filename = "report1.csv"'

    return response


#report N2

def report2(request):

    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Discount', 'Category', 'AVG_Disc', 'AVG'])

    sold = Sell.objects.filter(disc__category__isnull=False) #products with Category Discount
    sold_full_price = Sell.objects.filter(disc__category__isnull=True) #products without Category Discount

    fm = Sell.objects.aggregate(Max('time_of_purchase')) #the latest time of purchase
    fmin = Sell.objects.aggregate(Min('time_of_purchase')) #the earliest time of purchase
    delta=(fm['time_of_purchase__max']-fmin['time_of_purchase__min']).days #total days


    s = 0
    for i in sold:
        s+=i.amount_of_items #total sold items with Category Discount


    k = 0
    for i in sold_full_price:
        k+=i.amount_of_items #total sold items without Category Discount


    avg = s/delta #avg items sold with Category Discount per day
    avg_full_price = k/delta #avg items sold without Category Discount per day

#table
    for p in Sell.objects.filter(disc__category__isnull=False).values_list('disc__disc_title', 'disc__category__category'):
        writer.writerow([p[0],p[1], avg, avg_full_price])


    response['Content-Disposition'] = 'attachment; filename = "report2.csv"'

    return response

#report N3

def report3(request):

    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Discount', 'Product', 'AVG_Disc', 'AVG'])

    sold = Sell.objects.filter(disc__isnull=False) #products with Discount
    sold_full_price = Sell.objects.filter(disc__isnull=True) #products without Discount

    fm = Sell.objects.aggregate(Max('time_of_purchase')) #the latest time of purchase
    fmin = Sell.objects.aggregate(Min('time_of_purchase')) #the earliest time of purchase
    delta=(fm['time_of_purchase__max']-fmin['time_of_purchase__min']).days #total days

    s = 0
    for i in sold:
        s+=i.amount_of_items #total sold items with Discount


    k = 0
    for i in sold_full_price:
        k+=i.amount_of_items #total sold items without Discount


    avg = s/delta #avg items sold with Discount per day
    avg_full_price = k/delta #avg items sold without Discount per day

#table
    for p in Sell.objects.filter(disc__isnull=False).values_list('disc__disc_title', 'product__item'):
        writer.writerow([p[0],p[1], avg, avg_full_price])


    response['Content-Disposition'] = 'attachment; filename = "report3.csv"'

    return response

