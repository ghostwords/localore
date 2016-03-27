# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_auto_20160325_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutmissionpage',
            name='description_bottom',
        ),
        migrations.RemoveField(
            model_name='aboutmissionpage',
            name='description_top',
        ),
        migrations.AddField(
            model_name='aboutmissionpage',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
