# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20160328_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='video_poster_image',
            field=models.ForeignKey(verbose_name='poster image', null=True, related_name='+', to='localore_admin.LocaloreImage', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
