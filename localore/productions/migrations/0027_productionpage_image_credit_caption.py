# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0026_auto_20160408_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionpage',
            name='image_credit_caption',
            field=wagtail.wagtailcore.fields.RichTextField(verbose_name='credit caption', blank=True),
        ),
    ]
