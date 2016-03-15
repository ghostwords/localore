# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0014_productionpagerelatedperson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionpagerelatedperson',
            name='person',
            field=models.ForeignKey(verbose_name='Name', to='people.Person', related_name='+'),
        ),
    ]
