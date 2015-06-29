# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DeveloperProjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=255)),
                ('launch_date_month', models.CharField(default=b'', max_length=20)),
                ('launch_date_year', models.CharField(default=b'', max_length=4)),
                ('possession_date_month', models.CharField(default=b'', max_length=20)),
                ('possession_date_year', models.CharField(default=b'', max_length=4)),
                ('location', models.CharField(default=b'', max_length=255)),
                ('other_status', models.CharField(default=b'', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('pan_number', models.CharField(default=None, max_length=20)),
                ('date_of_purchase', models.CharField(default=None, max_length=20)),
                ('loan_from', models.CharField(default=None, max_length=20)),
                ('cost_of_purchase', models.CharField(default=0, max_length=20)),
                ('is_resale', models.BooleanField(default=False)),
                ('name_of_seller', models.CharField(default=None, max_length=255)),
                ('contact_number_seller', models.CharField(default=None, max_length=30)),
                ('email_seller', models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('launch_date', models.CharField(max_length=20)),
                ('possession_date', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('property_type', models.CharField(default=b'Apartment', max_length=255)),
                ('specifications', models.CharField(default=b'Basic', max_length=255)),
                ('built_up_area', models.CharField(max_length=6)),
                ('total_area', models.CharField(max_length=6)),
                ('number_of_bedrooms', models.CharField(default=1, max_length=3)),
                ('number_of_bathrooms', models.CharField(default=1, max_length=3)),
                ('number_of_parking_spaces', models.CharField(default=0, max_length=2)),
                ('address_line_one', models.CharField(max_length=255)),
                ('address_line_two', models.CharField(default=None, max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('pin_code', models.CharField(max_length=20)),
                ('connectivity', models.CharField(default=None, max_length=255)),
                ('neighborhood_quality', models.CharField(default=None, max_length=255)),
                ('comments', models.CharField(default=None, max_length=255)),
                ('developer', models.ForeignKey(to='properties.Developer')),
            ],
        ),
    ]
