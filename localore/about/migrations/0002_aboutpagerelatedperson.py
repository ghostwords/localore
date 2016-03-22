# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_auto_20160321_1805'),
        ('about', '0001_initial'),
        # had to be specified manually to fix migrations errors
        ('localore_admin', '0003_auto_20160316_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPageRelatedPerson',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('sort_order', models.IntegerField(editable=False, null=True, blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='related_people', to='about.AboutPage')),
                ('person', models.ForeignKey(verbose_name='Name', related_name='+', to='people.Person')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
