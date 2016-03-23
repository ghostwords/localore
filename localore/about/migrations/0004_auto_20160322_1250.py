# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_auto_20160321_1805'),
        ('about', '0003_auto_20160322_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPageRelatedPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('sort_order', models.IntegerField(null=True, blank=True, editable=False)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='AboutTeamPage',
            new_name='AboutPage',
        ),
        migrations.RemoveField(
            model_name='aboutteampagerelatedperson',
            name='page',
        ),
        migrations.RemoveField(
            model_name='aboutteampagerelatedperson',
            name='person',
        ),
        migrations.DeleteModel(
            name='AboutTeamPageRelatedPerson',
        ),
        migrations.AddField(
            model_name='aboutpagerelatedperson',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_people', to='about.AboutPage'),
        ),
        migrations.AddField(
            model_name='aboutpagerelatedperson',
            name='person',
            field=models.ForeignKey(related_name='+', to='people.Person', verbose_name='Name'),
        ),
    ]
