# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0032_projectpermission_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='date_of_purchase',
            new_name='estimted_posession_date',
        ),
        migrations.AddField(
            model_name='owner',
            name='original_date',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
