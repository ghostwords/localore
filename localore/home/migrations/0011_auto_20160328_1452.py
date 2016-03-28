# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20160328_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='related_content_title',
            field=models.CharField(verbose_name='title', max_length=255),
        ),
    ]
