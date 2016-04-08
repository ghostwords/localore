# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatches', '0006_auto_20160405_1010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dispatchesindexpage',
            options={'verbose_name': 'Dispatches Index'},
        ),
        migrations.AlterModelOptions(
            name='dispatchpage',
            options={'verbose_name': 'Dispatch'},
        ),
    ]
