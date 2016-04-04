# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatches', '0003_auto_20160403_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatchesindexpage',
            name='default_dispatch_type',
            field=models.CharField(default='v', choices=[('v', 'Video'), ('a', 'Audio'), ('s', 'Series')], max_length=1),
        ),
        migrations.AlterField(
            model_name='dispatchpage',
            name='dispatch_type',
            field=models.CharField(default='v', choices=[('v', 'Video'), ('a', 'Audio'), ('s', 'Series')], max_length=1),
        ),
    ]
