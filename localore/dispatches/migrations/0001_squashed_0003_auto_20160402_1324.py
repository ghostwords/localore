# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('dispatches', '0001_initial'), ('dispatches', '0002_auto_20160326_1019'), ('dispatches', '0003_auto_20160402_1324')]

    dependencies = [
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('localore_admin', '0004_pagealias'),
        ('wagtailcore', '0028_merge'),
        ('wagtailforms', '0003_capitalizeverbose'),
    ]

    operations = [
    ]
