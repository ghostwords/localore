# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20160413_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='is_featured',
            field=models.BooleanField(default=False, help_text='Makes this connection go to the top of the list on the connections index page.', verbose_name='featured'),
        ),
    ]
