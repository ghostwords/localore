# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0024_auto_20160402_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionpagerelatedlink',
            name='service_name',
            field=models.CharField(blank=True, verbose_name='service', max_length=10, choices=[('', 'Other'), ('facebook', 'Facebook'), ('instagram', 'Instagram'), ('soundcloud', 'SoundCloud'), ('tumblr', 'Tumblr'), ('twitter', 'Twitter'), ('vimeo', 'Vimeo'), ('youtube', 'YouTube')]),
        ),
    ]
