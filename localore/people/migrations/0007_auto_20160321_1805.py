# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0019_productionpagefeaturedperson'),
        ('people', '0006_auto_20160318_1718'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'people', 'ordering': ('-production', 'first_name', 'last_name'), 'verbose_name': 'person'},
        ),
        migrations.AddField(
            model_name='person',
            name='production',
            field=models.ForeignKey(null=True, blank=True, related_name='+', to='productions.ProductionPage', on_delete=django.db.models.deletion.SET_NULL, help_text='Leave blank for AIR/Localore staff.', verbose_name='associated production'),
        ),
    ]
