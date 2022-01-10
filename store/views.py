from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Min, Max, Sum, F

from .models import Product
from .models import Sell
from .models import Discount



from datetime import datetime, timedelta

from django.utils import timezone

from django.utils.translation import gettext as _

import csv

#start page
def index(request):

    return render(request, 'store/index.html')


#report N1

def report1(request):
    start_date = request.GET.get('start_date', '2021-12-03')
    start_date = datetime.strptime(start_date,'%Y-%m-%d')
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow([_('Time'), _('Name'), _('Price'), _('Discount'), _('Discount Amount')])

    data = Sell.objects.filter(time_of_purchase__range = [start_date, start_date + timedelta(days=1)]).annotate(discount_amount=F('product__price') * F('discount__value') / 100).values_list('time_of_purchase', 'product__name', 'product__price', 'discount__title', 'discount_amount')

    writer.writerows(data)

    response['Content-Disposition'] = 'attachment; filename = "report1.csv"'

    return response


#report N2

def report2(request):

    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow([_('Discount'), _('Category'), _('AVG_Discount'), _('AVG')])
    #time calculations
    fm = Sell.objects.aggregate(Max('time_of_purchase'))
    fmin = Sell.objects.aggregate(Min('time_of_purchase'))
    delta=(fm['time_of_purchase__max']-fmin['time_of_purchase__min']).days

    #categories with discounts
    for cat in list(Discount.objects.filter(category__isnull=False).values_list('category__category', flat = True)):
        #calculations for each category
        #sold with discounts
        avg_discount = Sell.objects.filter(discount__category__isnull=False).filter(discount__category__category = cat).aggregate(Sum('amount_of_items'))['amount_of_items__sum'] / delta
        #sold without discounts
        avg = Sell.objects.filter(discount__category__isnull=True).filter(product__category__category = cat).aggregate(Sum('amount_of_items'))['amount_of_items__sum'] / delta
        name = Discount.objects.filter(category__isnull=False).get(category__category = cat)

        writer.writerow([name, cat, avg_discount, avg])

    response['Content-Disposition'] = 'attachment; filename = "report2.csv"'
    return response

#report N3

def report3(request):

    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow([_('Discount'), _('Product'), _('AVG_Discount'), _('AVG')])

    #time calculations
    fm = Sell.objects.aggregate(Max('time_of_purchase')) #the latest time of purchase
    fmin = Sell.objects.aggregate(Min('time_of_purchase')) #the earliest time of purchase
    delta=(fm['time_of_purchase__max']-fmin['time_of_purchase__min']).days #total days

    #all discounts
    for disc in list(Discount.objects.values_list('id', flat=True)):
        discount = Discount.objects.get(id=disc)

        #no one item was sold with a such discount
        if list(Sell.objects.filter(discount = disc))==[]:
            avg_discount = 0
            avg = Sell.objects.aggregate(Sum('amount_of_items'))['amount_of_items__sum'] / delta
            product = "All items"
            writer.writerow([discount, product, avg_discount, avg])

        else:
            #products
            for prod in list(Sell.objects.filter(discount = disc).values_list('product', flat=True).distinct()):
                product = Product.objects.get(id=prod)

                #no one item was sold without this discount
                if list(Sell.objects.filter(product=prod).filter(discount__isnull=True))==[]:
                    avg = 0
                    avg_discount = Sell.objects.filter(product=prod).filter(discount=disc).aggregate(Sum('amount_of_items'))['amount_of_items__sum'] / delta

                else:
                    avg = Sell.objects.filter(product=prod).filter(discount__isnull=True).aggregate(Sum('amount_of_items'))['amount_of_items__sum'] / delta
                    avg_discount = Sell.objects.filter(product=prod).filter(discount=disc).aggregate(Sum('amount_of_items'))['amount_of_items__sum'] / delta

                writer.writerow([discount, product, avg_discount, avg])

    response['Content-Disposition'] = 'attachment; filename = "report3.csv"'

    return response

