# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20160325_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='subtitle',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
