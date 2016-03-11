# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0003_auto_20160310_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionpagerelatedlink',
            name='social_site',
            field=models.CharField(max_length=10, choices=[('', 'Other'), ('instagram', 'Instagram'), ('soundcloud', 'SoundCloud'), ('tumblr', 'Tumblr'), ('twitter', 'Twitter'), ('vine', 'Vine'), ('youtube', 'YouTube')], default=''),
            preserve_default=False,
        ),
    ]
