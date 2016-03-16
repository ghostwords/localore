# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20160224_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='main_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='localore_admin.LocaloreImage'),
        ),
    ]
