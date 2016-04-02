# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0023_auto_20160402_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionpage',
            name='tile_image',
            field=models.ForeignKey(null=True, blank=True, to='localore_admin.LocaloreImage', related_name='+', help_text='Optional: The image to use on the grid view of the productions index page. Will use hero image if not set.', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
