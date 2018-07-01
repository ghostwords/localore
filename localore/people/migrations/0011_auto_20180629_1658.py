# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0010_auto_20160516_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='production',
            field=models.ForeignKey(null=True, verbose_name='associated production', related_name='+', blank=True, on_delete=django.db.models.deletion.SET_NULL, help_text='Leave blank for Finding America and #LocaloreLive staff.', to='productions.ProductionPage'),
        ),
    ]
