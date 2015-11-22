from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse

from spares_info import models


def index(request):

    return render_to_response('spares_info/index.html')


def info(request):

    return render_to_response('spares_info/info.html')


def contacts(request):

    return render_to_response('spares_info/contacts.html')


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


def catalog(request):

    return render_to_response('spares_info/catalog.html')
