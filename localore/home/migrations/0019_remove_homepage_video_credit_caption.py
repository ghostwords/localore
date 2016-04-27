# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_homepage_video_credit_caption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='video_credit_caption',
        ),
    ]
