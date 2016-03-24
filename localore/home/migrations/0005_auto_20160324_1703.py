# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0007_merge'),
        ('localore_admin', '0004_pagealias'),
        ('home', '0004_auto_20151106_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='video_mp4',
            field=models.ForeignKey(to='wagtaildocs.Document', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='video_ogv',
            field=models.ForeignKey(to='wagtaildocs.Document', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='video_poster_image',
            field=models.ForeignKey(to='localore_admin.LocaloreImage', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='video_webm',
            field=models.ForeignKey(to='wagtaildocs.Document', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+'),
        ),
    ]
