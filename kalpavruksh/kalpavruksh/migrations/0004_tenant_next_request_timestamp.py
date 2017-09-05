# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kalpavruksh', '0003_auto_20170904_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='next_request_timestamp',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
