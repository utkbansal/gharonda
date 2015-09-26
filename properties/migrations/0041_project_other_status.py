# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0040_tower_added_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='other_status',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
