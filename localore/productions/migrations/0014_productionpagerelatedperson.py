# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20160310_2235'),
        ('productions', '0013_auto_20160314_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionPageRelatedPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='related_people', to='productions.ProductionPage')),
                ('person', models.ForeignKey(related_name='+', to='people.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
