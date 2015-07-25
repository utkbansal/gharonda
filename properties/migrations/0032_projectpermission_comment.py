# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0031_auto_20150724_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpermission',
            name='comment',
            field=models.TextField(default=None, null=True),
        ),
    ]
