# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('president', '0002_auto_20161121_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presidentpage',
            name='hero_image',
            field=models.ForeignKey(to='localore_admin.LocaloreImage', help_text='Optional: The header/hero/feature image for this President Series post.', related_name='+', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
