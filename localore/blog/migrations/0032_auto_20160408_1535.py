# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_blogpage_tile_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogindexpage',
            options={'verbose_name': 'Connections Index'},
        ),
        migrations.AlterModelOptions(
            name='blogpage',
            options={'verbose_name': 'Connection'},
        ),
    ]
