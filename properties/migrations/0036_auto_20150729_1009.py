# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0035_auto_20150729_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='estimted_posession_date',
            new_name='date_of_purchase',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='original_date',
        ),
    ]
