# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0018_auto_20150622_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('floors_completed', models.IntegerField(default=0)),
                ('finishing_status', models.CharField(max_length=255)),
                ('other_status', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'')),
                ('project', models.ForeignKey(to='properties.Project')),
            ],
        ),
    ]
