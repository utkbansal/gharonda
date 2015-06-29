# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ajaximage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0022_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developerproject',
            name='launch_date',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='developerproject',
            name='location',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='developerproject',
            name='other_status',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='developerproject',
            name='possession_date',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='occupation',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tower',
            name='finishing_status',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tower',
            name='image',
            field=ajaximage.fields.AjaxImageField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tower',
            name='other_status',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
