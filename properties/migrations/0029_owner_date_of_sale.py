# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0028_auto_20150716_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='date_of_sale',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
