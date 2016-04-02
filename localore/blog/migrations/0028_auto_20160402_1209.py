# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20160402_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='video_poster_image',
            field=models.ForeignKey(verbose_name='poster image', null=True, related_name='+', to='localore_admin.LocaloreImage', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
