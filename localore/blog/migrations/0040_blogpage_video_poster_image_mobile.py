# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localore_admin', '0005_auto_20160331_1015'),
        ('blog', '0039_blogpage_video_credit_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='video_poster_image_mobile',
            field=models.ForeignKey(to='localore_admin.LocaloreImage', null=True, related_name='+', verbose_name='poster image (mobile)', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
