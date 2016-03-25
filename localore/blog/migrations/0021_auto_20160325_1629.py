# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_blogpageassociatedproduction_blogpagerelatedconnection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogindexpage',
            old_name='body',
            new_name='intro',
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
