# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20151107_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexrelatedlink',
            name='link_external',
            field=models.URLField(blank=True, verbose_name='External link', max_length=500),
        ),
    ]
