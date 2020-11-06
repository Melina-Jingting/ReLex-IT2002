from django.db import models

# Create your models here.

from AppSeeker.models import Seeker, SeekerSkill
from AppCompany.models import Job


class Apply(models.Model):
    seeker = models.ForeignKey(Seeker, models.DO_NOTHING, db_column='seeker', primary_key=True)
    job = models.ForeignKey(Job, models.DO_NOTHING)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apply'
        unique_together = (('seeker', 'job'),)

class Likes(models.Model):
    seeker = models.ForeignKey(Seeker, models.DO_NOTHING, db_column='seeker', primary_key=True)
    job = models.ForeignKey(Job, models.DO_NOTHING)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'likes'
        unique_together = (('seeker', 'job'),)
