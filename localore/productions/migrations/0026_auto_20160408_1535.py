# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0025_auto_20160404_1629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productionpage',
            options={'verbose_name': 'Production'},
        ),
        migrations.AlterModelOptions(
            name='productionsindexpage',
            options={'verbose_name': 'Productions Index'},
        ),
    ]
