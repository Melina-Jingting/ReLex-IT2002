from django.db import models
from AppAccount.models import Account


# Create your models here.

class Company(models.Model):
    email = models.ForeignKey(Account, models.DO_NOTHING, db_column='email', primary_key=True)
    name = models.CharField(max_length=64)
    industry = models.CharField(max_length=64, blank=True, null=True)
    location = models.CharField(max_length=64, blank=True, null=True)
    size = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'

class Job(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    company = models.ForeignKey(Company, models.DO_NOTHING, db_column='company', blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    type = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=16000, blank=True, null=True)
    date_posted = models.DateField(blank=True, null=True)
    date_closing = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job'


class JobSkill(models.Model):
    job = models.ForeignKey(Job, models.DO_NOTHING, primary_key=True)
    skill = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'job_skill'
        unique_together = (('job', 'skill'),)

