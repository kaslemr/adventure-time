from django.db import models

# Create your models here.

class Respondent(models.Model):
    case_id = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    activity_totals = models.ManyToManyField(Activity)


class Activity(models.Model):
    code = models.IntegerField()
    daily_minutes = models.IntegerField()
    total_respondents = models.IntegerField()
    activity_title = models.CharField(100)

