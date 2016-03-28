# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20160328_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='video_youtube_id',
            field=models.CharField(max_length=12, verbose_name='YouTube video ID', default='j6IIjLK-8fU'),
        ),
    ]
