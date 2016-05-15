# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityresponse',
            name='title',
        ),
        migrations.AlterField(
            model_name='activityresponse',
            name='code',
            field=models.ForeignKey(to='atus.ActivityTitle'),
        ),
    ]
