# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0002_productionsindexpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionPageRelatedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('link', models.URLField(verbose_name='External link')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='productionpage',
            name='instagram_url',
        ),
        migrations.RemoveField(
            model_name='productionpage',
            name='soundcloud_url',
        ),
        migrations.RemoveField(
            model_name='productionpage',
            name='tumblr_url',
        ),
        migrations.RemoveField(
            model_name='productionpage',
            name='twitter_url',
        ),
        migrations.RemoveField(
            model_name='productionpage',
            name='vine_url',
        ),
        migrations.RemoveField(
            model_name='productionpage',
            name='youtube_url',
        ),
        migrations.AddField(
            model_name='productionpagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='productions.ProductionPage'),
        ),
    ]
