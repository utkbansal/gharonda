# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0026_auto_20150706_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='developer_report',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='permit_report',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
