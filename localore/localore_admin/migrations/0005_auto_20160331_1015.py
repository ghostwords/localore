# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localore_admin', '0004_pagealias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagealias',
            name='link_external',
            field=models.CharField(help_text='Please provide an external URL, or select a page below.', verbose_name='External link', max_length=500, blank=True),
        ),
    ]
