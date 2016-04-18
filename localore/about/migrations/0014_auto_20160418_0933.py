# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0013_aboutmissionpage_org_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmissionpage',
            name='org_description',
            field=wagtail.wagtailcore.fields.RichTextField(verbose_name='Organizational Description'),
        ),
    ]
