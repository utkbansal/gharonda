# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0034_auto_20150729_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='built_up_area',
            new_name='plot_area',
        ),
        migrations.AlterField(
            model_name='owner',
            name='is_resale',
            field=models.BooleanField(default=False, choices=[(False, b'Direct Builder'), (True, b'Re-Sale')]),
        ),
    ]
