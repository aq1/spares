from django.contrib import admin

from spares_info import models


@admin.register(models.Shop)
class ShopAdmin(admin.ModelAdmin):

    list_display = ['get_address_string', 'photo']
