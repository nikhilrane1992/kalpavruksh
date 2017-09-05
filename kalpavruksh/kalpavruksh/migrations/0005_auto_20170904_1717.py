# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kalpavruksh', '0004_tenant_next_request_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='next_request_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 17, 17, 54, 13255)),
        ),
    ]
