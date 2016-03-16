# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0016_auto_20160314_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, help_text='The header/hero/feature image for this production.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='localore_admin.LocaloreImage'),
        ),
        migrations.AlterField(
            model_name='productionpage',
            name='logo_image',
            field=models.ForeignKey(blank=True, help_text="The production's logo (optional).", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='localore_admin.LocaloreImage'),
        ),
    ]
