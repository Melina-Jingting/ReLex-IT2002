from django.db import models
from AppPages.models import Account

# Create your models here.
class Seeker(models.Model):
    email = models.ForeignKey(Account, models.DO_NOTHING, db_column='email', primary_key=True)
    name = models.CharField(max_length=256)
    industry = models.CharField(max_length=64, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'seeker'


class SeekerSkill(models.Model):
    seeker = models.ForeignKey(Seeker, models.DO_NOTHING, db_column='seeker', primary_key=True)
    skill = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'seeker_skill'
        unique_together = (('seeker', 'skill'),)