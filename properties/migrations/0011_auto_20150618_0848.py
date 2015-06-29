# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_auto_20150618_0750'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterField(
            model_name='property',
            name='address_line_two',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
