# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def add_banks(apps, schema_editor):
    Bank = apps.get_model('properties', 'Bank')
    banks = [
        'SBI',
        'Bank of Baroda',
        'Union Bank',
        'Yes Bank',
        'ICICI',
        'HDFC',
        'Punjab National Bank',
        'Canara Bank',
        'Union Bank of India',
        'IDBI Bank',
        'Kotak Mahindra Bank',
        'Axis Bank',
    ]

    for bank_name in banks:
        b = Bank(name=bank_name)
        b.save()


class Migration(migrations.Migration):
    dependencies = [
        ('properties', '0033_auto_20150725_0804'),
    ]

    operations = [
        migrations.RunPython(add_banks),
    ]
