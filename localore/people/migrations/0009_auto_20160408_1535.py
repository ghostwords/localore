# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20160325_1748'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Person', 'ordering': ('last_name',), 'verbose_name_plural': 'People'},
        ),
    ]
