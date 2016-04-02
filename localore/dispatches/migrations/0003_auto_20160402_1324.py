# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailcore', '0028_merge'),
        ('dispatches', '0002_auto_20160326_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiodispatchesindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='audiodispatchpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='videodispatchesindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='videodispatchpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='videodispatchpage',
            name='video',
        ),
        migrations.DeleteModel(
            name='AudioDispatchesIndexPage',
        ),
        migrations.DeleteModel(
            name='AudioDispatchPage',
        ),
        migrations.DeleteModel(
            name='VideoDispatchesIndexPage',
        ),
        migrations.DeleteModel(
            name='VideoDispatchPage',
        ),
    ]
