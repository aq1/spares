from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict

from spares_info import models


def index(request):

    return render_to_response('spares_info/index.html')


def info(request):

    return render_to_response('spares_info/info.html')


def contacts(request):

    return render_to_response('spares_info/contacts.html')


def shops(request, pk=None):

    if not pk:
        return render_to_response('spares_info/shops.html')
    else:
        try:
            shop = models.Shop.objects.get(pk=pk)
        except models.Shop.DoesNotExist:
            return redirect(reverse('shops'))

        context = {'shop': model_to_dict(shop)}
        return render_to_response('spares_info/shop.html', context)


def catalog(request):

    return render_to_response('spares_info/catalog.html')
