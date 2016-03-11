# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0008_auto_20160310_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionpagerelatedlink',
            name='service_name',
            field=models.CharField(max_length=10, choices=[('', 'Other'), ('instagram', 'Instagram'), ('soundcloud', 'SoundCloud'), ('tumblr', 'Tumblr'), ('twitter', 'Twitter'), ('vine', 'Vine'), ('youtube', 'YouTube')], verbose_name='service', blank=True),
        ),
        migrations.AlterField(
            model_name='productionpagerelatedlink',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
    ]
