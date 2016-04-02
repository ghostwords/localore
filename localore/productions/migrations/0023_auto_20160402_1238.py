# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0022_productionpage_tile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionpage',
            name='tile_image',
            field=models.ForeignKey(help_text='The image to use on the grid view of the productions index page.', to='localore_admin.LocaloreImage', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', blank=True),
        ),
    ]
