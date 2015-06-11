# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20150611_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='comments',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='connectivity',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='neighborhood_quality',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
