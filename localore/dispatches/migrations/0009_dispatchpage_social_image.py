# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localore_admin', '0008_auto_20160515_1150'),
        ('dispatches', '0008_auto_20160422_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispatchpage',
            name='social_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='localore_admin.LocaloreImage', related_name='+', help_text='Optional. The image to use when sharing the page on social networks.', blank=True),
        ),
    ]
