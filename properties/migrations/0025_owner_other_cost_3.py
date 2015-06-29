# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0024_owner_loan_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='other_cost_3',
            field=models.IntegerField(default=0),
        ),
    ]
