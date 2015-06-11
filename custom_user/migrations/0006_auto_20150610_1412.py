# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0005_auto_20150610_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brokerprofile',
            name='license_no',
            field=models.CharField(max_length=255),
        ),
    ]
