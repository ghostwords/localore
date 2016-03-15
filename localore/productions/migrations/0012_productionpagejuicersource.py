# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0011_auto_20160314_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionPageJuicerSource',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('source_name', models.CharField(max_length=100, help_text='Juicer source account name, without # or @. Filters across all account types in the feed.', verbose_name='source account name')),
                ('page', modelcluster.fields.ParentalKey(to='productions.ProductionPage', related_name='juicer_sources')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
