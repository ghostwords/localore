# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localore_admin', '0005_auto_20160331_1015'),
        ('blog', '0030_auto_20160404_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='tile_image',
            field=models.ForeignKey(blank=True, related_name='+', help_text='Optional: The image to use on the connections index page. Will use poster image if not set.', on_delete=django.db.models.deletion.SET_NULL, null=True, to='localore_admin.LocaloreImage'),
        ),
    ]
