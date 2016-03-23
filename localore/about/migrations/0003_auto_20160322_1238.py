# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0007_auto_20160321_1805'),
        ('about', '0002_aboutpagerelatedperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTeamPageRelatedPerson',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, null=True, editable=False)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
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
            field=models.ForeignKey(verbose_name='Name', related_name='+', to='people.Person'),
        ),
    ]
