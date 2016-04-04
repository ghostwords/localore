# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('localore_admin', '0005_auto_20160331_1015'),
        ('dispatches', '0002_dispatchesindexpage_dispatchpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispatchpage',
            name='poster_image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, null=True, to='localore_admin.LocaloreImage'),
        ),
        migrations.AlterField(
            model_name='dispatchpage',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='dispatchpage',
            name='embed_url',
            field=models.URLField(verbose_name='Embed URL', help_text='YouTube or SoundCloud'),
        ),
    ]
