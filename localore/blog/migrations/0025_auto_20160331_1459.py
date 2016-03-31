# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_blogpage_intro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpage',
            old_name='main_image',
            new_name='video_poster_image',
        ),
    ]
