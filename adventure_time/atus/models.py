from django.db import models

# Create your models here.

class Respondent(models.Model):
    respondent = models.IntegerField()
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
    #code = models.ForeignKey("ActivityTitle")

    def __str__(self):
        return str(self.respondent)

class HouseholdMember(models.Model):
    respondent = models.ForeignKey(Respondent)
    relative_id = models.IntegerField()
    age = models.IntegerField()
    relation = models.IntegerField()
    sex = models.IntegerField()


class ActivityTitle(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=75)

    def __str__(self):
        return str(self.code)

class ActivityResponse(models.Model):
    respondent = models.ForeignKey(Respondent)
    code = models.ForeignKey(ActivityTitle)
    minutes = models.IntegerField()
