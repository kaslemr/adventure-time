from django.db import models

# Create your models here.


class PersonInfo(models.Model):

    person_id = models.IntegerField()
    weight = models.IntegerField()
    youngest_child = models.IntegerField()
    age = models.IntegerField()
    sex = models.IntegerField()
    education = models.IntegerField()
    race = models.IntegerField()
    metro_status = models.IntegerField()
    labor_status = models.IntegerField()
    weekly_earnings = models.IntegerField()
