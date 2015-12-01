# -*- coding: UTF-8 -*-

from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from spares_info import models


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):

    list_display = ['get_address_string', 'photo']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['category', 'name', 'quantity', 'price']


@admin.register(models.Category)
class CategoryAdmin(MPTTModelAdmin):
    pass
