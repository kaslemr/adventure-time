# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityResponse',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('code', models.CharField(max_length=6)),
                ('minutes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ActivityTitle',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('code', models.CharField(max_length=6)),
                ('title', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='HouseholdMember',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('relative_id', models.IntegerField()),
                ('age', models.IntegerField()),
                ('relation', models.IntegerField()),
                ('sex', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Respondent',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('respondent', models.IntegerField()),
                ('weight', models.FloatField()),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField()),
                ('education', models.IntegerField()),
                ('race', models.IntegerField()),
                ('metro_status', models.IntegerField()),
                ('labor_status', models.IntegerField()),
                ('wkly_earnings', models.IntegerField()),
                ('multiple_job_status', models.IntegerField()),
                ('full_or_part_job_status', models.IntegerField()),
                ('school_enrollment', models.IntegerField()),
                ('school_level', models.IntegerField()),
                ('typical_work_hrs', models.IntegerField()),
                ('code', models.ForeignKey(to='atus.ActivityTitle')),
            ],
        ),
        migrations.AddField(
            model_name='householdmember',
            name='respondent',
            field=models.ForeignKey(to='atus.Respondent'),
        ),
        migrations.AddField(
            model_name='activityresponse',
            name='respondent',
            field=models.ForeignKey(to='atus.Respondent'),
        ),
        migrations.AddField(
            model_name='activityresponse',
            name='title',
            field=models.ForeignKey(to='atus.ActivityTitle'),
        ),
    ]
