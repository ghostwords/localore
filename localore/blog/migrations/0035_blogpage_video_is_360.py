# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20160413_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='video_is_360',
            field=models.BooleanField(help_text='This is a 360-degree video.', verbose_name='360˚ video', default=False),
        ),
    ]
