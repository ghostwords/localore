# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='production',
            field=models.ForeignKey(null=True, blank=True, help_text='Leave blank for AIR/Localore staff.', on_delete=django.db.models.deletion.SET_NULL, to='productions.ProductionPage', related_name='+', verbose_name='associated production'),
        ),
    ]
