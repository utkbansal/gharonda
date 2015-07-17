# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0029_owner_date_of_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='email_seller',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
    ]
