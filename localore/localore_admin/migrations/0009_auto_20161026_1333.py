# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailimages.models


class Migration(migrations.Migration):

    dependencies = [
        ('localore_admin', '0008_auto_20160515_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localorerendition',
            name='file',
            field=models.ImageField(height_field='height', upload_to=wagtail.wagtailimages.models.get_rendition_upload_to, width_field='width'),
        ),
    ]
