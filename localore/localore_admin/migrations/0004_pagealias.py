# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('localore_admin', '0003_auto_20160316_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageAlias',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, parent_link=True, to='wagtailcore.Page', primary_key=True, auto_created=True)),
                ('link_external', models.URLField(max_length=500, blank=True, help_text='Please provide an external URL, or select a page below.', verbose_name='External link')),
                ('link_page', models.ForeignKey(blank=True, related_name='+', on_delete=django.db.models.deletion.SET_NULL, to='wagtailcore.Page', verbose_name='Internal link', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
