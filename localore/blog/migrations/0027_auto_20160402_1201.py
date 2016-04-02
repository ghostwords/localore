# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20160331_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='video_youtube_id',
            field=models.CharField(verbose_name='YouTube video ID', max_length=12, blank=True, help_text='The part in bold: https://www.youtube.com/watch?v=<b>j6IIjLK-8fU</b>'),
        ),
    ]
