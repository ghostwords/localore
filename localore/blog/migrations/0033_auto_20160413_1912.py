# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20160408_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexrelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='blogindexrelatedlink',
            name='page',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='is_featured',
            field=models.BooleanField(verbose_name='featured', default=False),
        ),
        migrations.DeleteModel(
            name='BlogIndexRelatedLink',
        ),
    ]
