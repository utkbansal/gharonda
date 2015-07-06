# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0025_owner_other_cost_3'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PinCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.ForeignKey(to='properties.City'),
        ),
        migrations.AlterField(
            model_name='property',
            name='pin_code',
            field=models.ForeignKey(to='properties.PinCode'),
        ),
        migrations.AlterField(
            model_name='property',
            name='state',
            field=models.ForeignKey(to='properties.State'),
        ),
    ]
