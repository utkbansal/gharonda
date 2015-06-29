# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ajaximage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0020_property_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', ajaximage.fields.AjaxImageField()),
            ],
        ),
        migrations.AlterField(
            model_name='tower',
            name='image',
            field=ajaximage.fields.AjaxImageField(),
        ),
    ]
