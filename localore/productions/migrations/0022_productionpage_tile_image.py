# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localore_admin', '0005_auto_20160331_1015'),
        ('productions', '0021_auto_20160325_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionpage',
            name='tile_image',
            field=models.ForeignKey(related_name='+', to='localore_admin.LocaloreImage', null=True, blank=True, help_text='The image to use on the grid view productions index page.', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
