# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('localore_admin', '0005_auto_20160331_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleAnalytics',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('ga_tracking_id', models.CharField(max_length=20, verbose_name='Google Analytics tracking ID')),
                ('site', models.OneToOneField(to='wagtailcore.Site', editable=False)),
            ],
            options={
                'verbose_name': 'Google Analytics',
            },
        ),
    ]
