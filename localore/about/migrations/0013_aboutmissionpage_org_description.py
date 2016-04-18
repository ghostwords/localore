# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0012_auto_20160408_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmissionpage',
            name='org_description',
            field=wagtail.wagtailcore.fields.RichTextField(default='', verbose_name='About AIR'),
            preserve_default=False,
        ),
    ]
