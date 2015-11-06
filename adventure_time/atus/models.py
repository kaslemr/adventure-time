from django.db import models

# Create your models here.

class Respondent(models.Model):
    respondent = models.FloatField()
    weight = models.FloatField()
    age = models.IntegerField()
    sex = models.IntegerField()
    education = models.IntegerField()
    race = models.IntegerField()
    metro_status = models.IntegerField()
    labor_status = models.IntegerField()
    wkly_earnings = models.IntegerField()
    multiple_job_status = models.IntegerField()
    full_or_part_job_status = models.IntegerField()
    school_enrollment = models.IntegerField()
    school_level = models.IntegerField()
    typical_work_hrs = models.IntegerField()
    activity_code = models.ManyToManyField(ActivityCode, through='ActivityTitle')
    household = models.ManytoManyField(Household)


class Household(models.Model):
    respondent_id = models.ForeignKey(Respondent)
#   relative_id = models.IntegerField()
    age = models.IntegerField()
    relations = models.IntegerField()
    sex = models.IntegerField()


class ActivityTitles_(models.Model):
    code = models.IntegerField()
    title = models.CharField(max_length=75)


class ActivityResponses (models.Model):
    activity_code = models.IntegerField()
    minutes = models.IntegerField()


