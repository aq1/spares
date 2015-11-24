from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.db import IntegrityError

from spares_info import models


def index(request):

    return render_to_response('spares_info/index.html')


def info(request):

    return render_to_response('spares_info/info.html')


def contacts(request):

    return render_to_response('spares_info/contacts.html')


def catalog(request, pk=None):

    catalog = models.Category.objects.all().order_by('name')

    if pk:
        items = models.Product.objects.filter(category_id=pk)
    else:
        items = None

    return render_to_response('spares_info/catalog.html', {'catalog': catalog,
                                                           'selected': pk,
                                                           'items': items})


def shops(request, pk=None):

    if not pk:
        template = 'spares_info/shops.html'
        context = {'shops': models.Shop.get_all_shops()}
    else:
        try:
            shop = models.Shop.get_basic_info(pk=pk)
        except models.Shop.DoesNotExist:
            return redirect(reverse('shops'))

        context = {'shop': shop}
        template = 'spares_info/shop.html'

    return render_to_response(template, context)



def n(f):
    import csv
    import re
    import time



    j = 0
    r = re.compile('\d')
    # f = f.read().decode('cp1251')
    for i, row in enumerate(f.readlines()):
        row = row.decode('cp1251').split(',')
        # print(row)
        if not row[2] and row[1]:
            category = row[1]
            category_model, _ = models.Category.objects.get_or_create(name=category)
        else:
            rr = r.findall(row[2])
            price = '%s.%s' % (''.join(rr[:-2]), ''.join(rr[-2:]))
            try:
                price = float(price)
            except ValueError:
                j += 1
                print(i, category, row[1], price)
                continue

            try:
                models.Product.objects.get_or_create(category=category_model,
                                                     name=row[1],
                                                     price=price)
            except IntegrityError:
                print(i, category, row[1], price)


# @login_reqired
def catalog_upload(request):
    n(request.FILES['file'])

    return render_to_response('spares_info/catalog_upload_result.html',
                              {'r': request.FILES['file']})


def utils(request):

    return render_to_response('spares_info/utils.html',
                              context_instance=RequestContext(request))
