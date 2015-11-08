# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

from play import load_respondent_data, load_activity_title_data

class Migration(migrations.Migration):

    dependencies = [
        ('atus', '0002_auto_20151107_2255'),
    ]

    operations = [
        migrations.RunPython(load_activity_title_data)
    ]
