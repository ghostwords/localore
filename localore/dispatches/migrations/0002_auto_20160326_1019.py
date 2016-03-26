# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_embed_videos', '0003_auto_20150817_1256'),
        ('dispatches', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videodispatchpage',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='videodispatchpage',
            name='video',
            field=models.ForeignKey(verbose_name='Video', null=True, blank=True, to='wagtail_embed_videos.EmbedVideo', related_name='+', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
