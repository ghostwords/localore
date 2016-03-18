# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productions', '0017_auto_20160316_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productionpagejuicersource',
            name='name',
            field=models.CharField(verbose_name='source account or hashtag', help_text='Juicer source name, without # or @. Filters by account/hashtag within the feed across all services (Twitter, Facebook, ...).', max_length=100),
        ),
    ]
