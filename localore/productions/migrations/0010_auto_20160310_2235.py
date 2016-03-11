# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0009_auto_20160310_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionpagerelatedlink',
            name='service_name',
            field=models.CharField(blank=True, max_length=10, verbose_name='service', choices=[('', 'Other'), ('instagram', 'Instagram'), ('soundcloud', 'SoundCloud'), ('tumblr', 'Tumblr'), ('twitter', 'Twitter'), ('vimeo', 'Vimeo'), ('youtube', 'YouTube')]),
        ),
    ]
