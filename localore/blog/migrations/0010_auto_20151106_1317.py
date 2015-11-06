# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20151106_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexrelatedlink',
            name='link_page',
            field=models.ForeignKey(related_name='+', to='blog.BlogPage', null=True, blank=True),
        ),
    ]
