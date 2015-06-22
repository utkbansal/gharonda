# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0014_auto_20150622_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contractor_name_1',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='contractor_name_2',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='contractor_name_3',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
