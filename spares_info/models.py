from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):

    name = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True)


class Product(models.Model):

    category = models.ForeignKey(Category)
    name = models.CharField(max_length=1023, unique=True)
    quantity = models.PositiveIntegerField(blank=True, default=0)
    price = models.FloatField(blank=True, default=0)


class Shop(models.Model):

    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    housing = models.SmallIntegerField(blank=True, default=0)
    house = models.IntegerField()
    photo = models.ImageField(upload_to='shops/')

    def get_address_string(self):
        return '{}, ул. {} д. {}'.format(self.city, self.street, self.house)
