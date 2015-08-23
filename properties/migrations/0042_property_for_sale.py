# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0041_project_other_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='for_sale',
            field=models.BooleanField(default=False),
        ),
    ]
