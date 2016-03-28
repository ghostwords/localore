# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20160328_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='related_content_page',
            field=models.ForeignKey(verbose_name='destination', blank=True, to='wagtailcore.Page', related_name='+', null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
