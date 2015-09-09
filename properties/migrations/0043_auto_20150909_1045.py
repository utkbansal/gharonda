# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0042_property_for_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pincode',
            name='code',
            field=models.IntegerField(default=None, unique=True, null=True),
        ),
    ]
