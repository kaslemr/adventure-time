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
    activity_code = models.ManyToManyField(Activity)


class Activity(models.Model):
    respondent = models.ForeignKey(Respondent)
    activity_code = models.IntegerField()

    daily_minutes = models.IntegerField()
    total_respondents = models.IntegerField()
    activity_title = models.CharField(100)


class Household(models.Model):
    respondent = models.ForeignKey(Respondent)
    activity_code = models.IntegerField()
    minutes = models.IntegerField()


