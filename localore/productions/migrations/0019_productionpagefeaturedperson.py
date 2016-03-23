# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_auto_20160316_1520'),
        ('productions', '0018_auto_20160318_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionPageFeaturedPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', modelcluster.fields.ParentalKey(to='productions.ProductionPage', related_name='featured_people')),
                ('person', models.ForeignKey(to='people.Person', related_name='+', verbose_name='Name')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
