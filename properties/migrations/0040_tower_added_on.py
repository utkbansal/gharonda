# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0039_property_added_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='tower',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 10, 19, 5, 2, 701016, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
