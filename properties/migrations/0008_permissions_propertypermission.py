# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_auto_20150616_0709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.BooleanField()),
                ('permission', models.ForeignKey(to='properties.Permissions')),
                ('project', models.ForeignKey(to='properties.Project')),
            ],
        ),
    ]
