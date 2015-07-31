# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0036_auto_20150729_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='possession_date',
            new_name='estimated_possession_date',
        ),
        migrations.AddField(
            model_name='project',
            name='original_possession_date',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
