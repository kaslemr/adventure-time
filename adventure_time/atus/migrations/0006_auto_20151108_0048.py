# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from play import load_household_data


class Migration(migrations.Migration):

    dependencies = [
        ('atus', '0005_auto_20151108_0043'),
    ]

    operations = [
        migrations.RunPython(load_household_data)
    ]
