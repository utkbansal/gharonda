# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0027_auto_20150713_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='pin_code',
            field=models.ForeignKey(default=None, to='properties.PinCode', null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='state',
            field=models.ForeignKey(default=None, to='properties.State', null=True),
        ),
    ]
