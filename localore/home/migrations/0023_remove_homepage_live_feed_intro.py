# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_livefeedpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='live_feed_intro',
        ),
    ]
