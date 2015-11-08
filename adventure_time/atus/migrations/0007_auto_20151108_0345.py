# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from play import load_activity_response_data


class Migration(migrations.Migration):

    dependencies = [
        ('atus', '0006_auto_20151108_0048'),
    ]

    operations = [
        migrations.RunPython(load_activity_response_data)
    ]
