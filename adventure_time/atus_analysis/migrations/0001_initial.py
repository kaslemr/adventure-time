# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('person_id', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('youngest_child', models.IntegerField()),
                ('age', models.IntegerField()),
                ('sex', models.TextField()),
                ('education', models.IntegerField()),
                ('race', models.IntegerField()),
                ('metro_status', models.IntegerField()),
                ('labor_status', models.IntegerField()),
                ('weekly_earnings', models.IntegerField()),
            ],
        ),
    ]
