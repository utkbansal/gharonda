# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0006_auto_20150610_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactnumber',
            name='contact_type',
            field=models.CharField(default=b'Mobile', max_length=255),
        ),
    ]
