# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from play import get_summary_data_from_atus_data


class Migration(migrations.Migration):

    dependencies = [
        ('atus_analysis', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(get_summary_data_from_atus_data),
    ]
