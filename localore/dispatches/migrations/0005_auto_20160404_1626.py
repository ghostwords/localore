# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatches', '0004_auto_20160404_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatchesindexpage',
            name='default_dispatch_type',
            field=models.CharField(choices=[('v', 'Video'), ('a', 'Audio')], default='v', max_length=1),
        ),
        migrations.AlterField(
            model_name='dispatchpage',
            name='dispatch_type',
            field=models.CharField(choices=[('v', 'Video'), ('a', 'Audio')], default='v', max_length=1),
        ),
    ]
