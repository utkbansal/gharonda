# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0038_bank_by_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 10, 17, 37, 15, 875901, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
