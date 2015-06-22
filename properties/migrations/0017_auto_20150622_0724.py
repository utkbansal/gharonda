# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0016_developerprojects_number_of_projects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='cost_of_purchase',
            new_name='main_cost_of_purchase',
        ),
        migrations.AddField(
            model_name='owner',
            name='other_cost_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='owner',
            name='other_cost_2',
            field=models.IntegerField(default=0),
        ),
    ]
