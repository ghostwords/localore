# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20160325_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='site_intro',
        ),
        migrations.AddField(
            model_name='homepage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, default='Across America'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='video_poster_image',
            field=models.ForeignKey(related_name='+', null=True, on_delete=django.db.models.deletion.SET_NULL, to='localore_admin.LocaloreImage'),
        ),
    ]
