# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0013_property_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developerprojects',
            old_name='launch_date_month',
            new_name='launch_date',
        ),
        migrations.RenameField(
            model_name='developerprojects',
            old_name='possession_date_month',
            new_name='possession_date',
        ),
        migrations.RemoveField(
            model_name='developerprojects',
            name='launch_date_year',
        ),
        migrations.RemoveField(
            model_name='developerprojects',
            name='possession_date_year',
        ),
    ]
