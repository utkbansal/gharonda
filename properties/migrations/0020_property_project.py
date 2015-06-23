# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0019_tower'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='project',
            field=models.ForeignKey(default=1, to='properties.Project'),
            preserve_default=False,
        ),
    ]
