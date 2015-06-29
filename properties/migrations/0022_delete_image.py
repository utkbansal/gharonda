# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0021_auto_20150623_1018'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
