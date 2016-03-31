# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0010_auto_20160327_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmissionpagerelatedlink',
            name='link_external',
            field=models.CharField(help_text='Please provide an external URL, or select a page below.', verbose_name='External link', max_length=500, blank=True),
        ),
    ]
