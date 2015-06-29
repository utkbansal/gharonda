# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0011_auto_20150618_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='owner',
            field=models.ForeignKey(default=None, to='properties.Owner', null=True),
        ),
    ]
