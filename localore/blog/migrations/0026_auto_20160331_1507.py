# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0007_merge'),
        ('blog', '0025_auto_20160331_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='video_mp4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtaildocs.Document', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='video_ogv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtaildocs.Document', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='video_webm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtaildocs.Document', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='video_youtube_id',
            field=models.CharField(max_length=12, verbose_name='YouTube video ID', help_text='The part in bold: https://www.youtube.com/watch?v=<b>j6IIjLK-8fU</b>', default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='video_poster_image',
            field=models.ForeignKey(null=True, to='localore_admin.LocaloreImage', on_delete=django.db.models.deletion.SET_NULL, related_name='+'),
        ),
    ]
