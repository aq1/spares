# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spares_info', '0003_auto_20151122_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='map_url',
            field=models.CharField(blank=True, max_length=2047, default=''),
        ),
    ]
