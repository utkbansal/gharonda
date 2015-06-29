# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0023_auto_20150627_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='loan_status',
            field=models.BooleanField(default=False),
        ),
    ]
