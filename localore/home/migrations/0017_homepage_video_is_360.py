# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_homepage_site_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='video_is_360',
            field=models.BooleanField(help_text='This is a 360-degree video.', verbose_name='360˚ video', default=False),
        ),
    ]
