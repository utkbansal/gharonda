# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0004_auto_20150606_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactnumber',
            name='contact_no',
            field=models.CharField(max_length=255),
        ),
    ]
