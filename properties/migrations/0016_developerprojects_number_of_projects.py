# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0015_auto_20150622_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='developerprojects',
            name='number_of_projects',
            field=models.IntegerField(default=0),
        ),
    ]
