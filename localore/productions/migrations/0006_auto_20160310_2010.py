# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0005_auto_20160310_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionpagerelatedlink',
            name='site',
            field=models.CharField(choices=[('', 'Other'), ('instagram', 'Instagram'), ('soundcloud', 'SoundCloud'), ('tumblr', 'Tumblr'), ('twitter', 'Twitter'), ('vine', 'Vine'), ('youtube', 'YouTube')], blank=True, max_length=10),
        ),
    ]
