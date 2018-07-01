# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_auto_20180629_1658'),
        ('about', '0015_auto_20160531_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTeamPageRelatedLocaloreLivePerson',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
                ('page', modelcluster.fields.ParentalKey(related_name='related_localorelive_people', to='about.AboutTeamPage')),
                ('person', models.ForeignKey(related_name='+', to='people.Person', verbose_name='Name')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='aboutteampagerelatedperson',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_air_people', to='about.AboutTeamPage'),
        ),
    ]
