# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0019_verbose_names_cleanup'),
        ('blog', '0003_blogindexpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexRelatedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('link_external', models.URLField(verbose_name='External link', blank=True)),
                ('title', models.CharField(max_length=255, help_text='Link title')),
                ('link_page', models.ForeignKey(related_name='+', null=True, to='wagtailcore.Page', blank=True)),
                ('page', modelcluster.fields.ParentalKey(to='blog.BlogIndexPage', related_name='related_links')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
