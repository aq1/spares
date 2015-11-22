# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spares_info', '0002_shop_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='housing',
            field=models.SmallIntegerField(blank=True, default=0),
        ),
    ]
