# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0019_productionpagefeaturedperson'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionsindexpage',
            name='default_view',
            field=models.CharField(max_length=1, default='g', choices=[('g', 'Grid'), ('l', 'List')]),
        ),
    ]
