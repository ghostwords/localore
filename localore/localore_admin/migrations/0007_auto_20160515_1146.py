# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localore_admin', '0006_googleanalytics'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='juicersettings',
            options={'verbose_name': 'Juicer'},
        ),
    ]
