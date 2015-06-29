# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0008_permissions_propertypermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255)),
                ('permission', models.ForeignKey(to='properties.Permissions')),
                ('project', models.ForeignKey(to='properties.Project')),
            ],
        ),
        migrations.RemoveField(
            model_name='propertypermission',
            name='permission',
        ),
        migrations.RemoveField(
            model_name='propertypermission',
            name='project',
        ),
        migrations.DeleteModel(
            name='PropertyPermission',
        ),
    ]
