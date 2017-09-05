# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kalpavruksh', '0002_tenant_api_request_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to='kalpavruksh.User'),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to='kalpavruksh.User'),
        ),
    ]
