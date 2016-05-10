# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localore_admin', '0005_auto_20160331_1015'),
        ('home', '0019_remove_homepage_video_credit_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='video_poster_image_mobile',
            field=models.ForeignKey(to='localore_admin.LocaloreImage', null=True, related_name='+', verbose_name='poster image (mobile)', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
