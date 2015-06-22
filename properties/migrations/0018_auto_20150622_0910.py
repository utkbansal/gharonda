# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0017_auto_20150622_0724'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=255)),
                ('launch_date', models.CharField(default=b'', max_length=20)),
                ('possession_date', models.CharField(default=b'', max_length=20)),
                ('location', models.CharField(default=b'', max_length=255)),
                ('other_status', models.CharField(default=b'', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='developerprojects',
            name='developer',
        ),
        migrations.AddField(
            model_name='developer',
            name='number_of_projects',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='DeveloperProjects',
        ),
        migrations.AddField(
            model_name='developerproject',
            name='developer',
            field=models.ForeignKey(to='properties.Developer'),
        ),
    ]
