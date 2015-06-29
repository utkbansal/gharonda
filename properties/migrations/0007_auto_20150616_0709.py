# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_auto_20150612_0630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='owner',
            name='is_resale',
            field=models.BooleanField(default=False, choices=[(True, b'Re-Sale'), (False, b'Direct Builder')]),
        ),
        migrations.AddField(
            model_name='project',
            name='bank',
            field=models.ManyToManyField(to='properties.Bank'),
        ),
    ]
