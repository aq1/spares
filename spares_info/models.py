from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):

    name = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category)
    name = models.CharField(max_length=2047)
    quantity = models.PositiveIntegerField(blank=True, default=0)
    price = models.FloatField(blank=True, default=0)


class Shop(models.Model):

    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    housing = models.SmallIntegerField(blank=True, default=0)
    house = models.IntegerField()
    photo = models.ImageField(upload_to='shops/')
    map_url = models.CharField(max_length=2047, blank=True, default='')

    def get_address_string(self):
        return '{}, ул. {} д. {}'.format(self.city, self.street, self.house)

    @classmethod
    def get_all_shops(cls):
        return [{'id': shop.id,
                 'photo': shop.photo.url,
                 'address': shop.get_address_string()}
                for shop in cls.objects.all()]

    @classmethod
    def get_basic_info(cls, pk):
        shop = cls.objects.get(pk=pk)
        return {
            'id': shop.id,
            'address': shop.get_address_string(),
            'photo': shop.photo.url,
            'map': shop.map_url
        }
