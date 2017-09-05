# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kalpavruksh', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='api_request_count',
            field=models.IntegerField(default=0),
        ),
    ]
