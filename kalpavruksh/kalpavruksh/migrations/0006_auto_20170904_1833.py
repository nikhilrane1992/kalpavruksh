# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kalpavruksh', '0005_auto_20170904_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantAPICount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('api_request_count', models.IntegerField(default=0)),
                ('next_request_timestamp', models.DateTimeField(default=datetime.datetime(2017, 9, 4, 18, 33, 59, 851968))),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='api_request_count',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='next_request_timestamp',
        ),
        migrations.AddField(
            model_name='tenantapicount',
            name='tenant',
            field=models.ForeignKey(to='kalpavruksh.Tenant'),
        ),
    ]
