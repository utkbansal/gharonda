# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_owner_co_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='contact_number_seller',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='date_of_purchase',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='email_seller',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='loan_from',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='name_of_seller',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='pan_number',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
