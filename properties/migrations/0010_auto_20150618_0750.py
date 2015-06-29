# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0009_auto_20150617_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='built_up_area',
            field=models.FloatField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='property',
            name='developer',
            field=models.ForeignKey(default=None, to='properties.Developer', null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='total_area',
            field=models.FloatField(default=0),
        ),
    ]
