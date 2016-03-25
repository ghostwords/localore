# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20160324_1029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogindexpage',
            options={'verbose_name': 'connections index page'},
        ),
        migrations.AlterModelOptions(
            name='blogpage',
            options={'verbose_name': 'connection'},
        ),
    ]
