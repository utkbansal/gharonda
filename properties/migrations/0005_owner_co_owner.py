# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_developerprojects_developer'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='co_owner',
            field=models.ForeignKey(default=None, to='properties.Owner', null=True),
        ),
    ]
