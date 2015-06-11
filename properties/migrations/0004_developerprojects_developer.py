# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20150611_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='developerprojects',
            name='developer',
            field=models.ForeignKey(default=1, to='properties.Developer'),
            preserve_default=False,
        ),
    ]
