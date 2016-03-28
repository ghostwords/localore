# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20160328_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='view_more_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, verbose_name='Page to link to', to='wagtailcore.Page', related_name='+'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='view_more_title',
            field=models.CharField(verbose_name='"View more" link title', help_text='For example, "View more connections"', max_length=255),
        ),
    ]
