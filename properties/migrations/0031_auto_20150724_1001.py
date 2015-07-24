# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0030_auto_20150717_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='developerproject',
            name='address',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='developerproject',
            name='status',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
