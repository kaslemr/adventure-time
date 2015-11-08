# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atus', '0003_auto_20151107_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respondent',
            name='code',
        ),
        migrations.AlterField(
            model_name='activitytitle',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]
