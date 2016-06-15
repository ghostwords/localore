# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('home', '0023_remove_homepage_live_feed_intro'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageFeaturedPage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('title', models.CharField(blank=True, max_length=255, help_text='Leave blank to use page title.')),
                ('subtitle', models.CharField(max_length=255)),
                ('featured_page', models.ForeignKey(verbose_name='page to feature', to='wagtailcore.Page', related_name='+')),
                ('home_page', modelcluster.fields.ParentalKey(to='home.HomePage', related_name='featured_pages')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
    ]
