# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from play import load_respondent_data


class Migration(migrations.Migration):

    dependencies = [
        ('atus', '0004_auto_20151108_0042'),
    ]

    operations = [
        migrations.RunPython(load_respondent_data)
    ]