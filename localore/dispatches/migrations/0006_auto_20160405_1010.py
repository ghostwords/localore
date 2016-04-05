# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatches', '0005_auto_20160404_1626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dispatchpage',
            options={'verbose_name': 'dispatch'},
        ),
    ]
