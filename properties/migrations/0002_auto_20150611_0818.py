# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='built_up_area',
            field=models.FloatField(max_length=6),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_area',
            field=models.FloatField(),
        ),
    ]
