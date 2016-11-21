# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('president', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presidentindexpage',
            old_name='share_your_store_text',
            new_name='share_your_story_text',
        ),
    ]
