# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_auto_20160321_1805'),
        ('about', '0004_auto_20160322_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTeamPageRelatedPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, blank=True, editable=False)),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
        migrations.RenameModel(
            old_name='AboutPage',
            new_name='AboutTeamPage',
        ),
        migrations.RemoveField(
            model_name='aboutpagerelatedperson',
            name='page',
        ),
        migrations.RemoveField(
            model_name='aboutpagerelatedperson',
            name='person',
        ),
        migrations.DeleteModel(
            name='AboutPageRelatedPerson',
        ),
        migrations.AddField(
            model_name='aboutteampagerelatedperson',
            name='page',
            field=modelcluster.fields.ParentalKey(to='about.AboutTeamPage', related_name='related_people'),
        ),
        migrations.AddField(
            model_name='aboutteampagerelatedperson',
            name='person',
            field=models.ForeignKey(to='people.Person', related_name='+', verbose_name='Name'),
        ),
    ]
