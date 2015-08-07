# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0037_auto_20150731_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='by_admin',
            field=models.BooleanField(default=True),
        ),
    ]
