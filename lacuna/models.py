from django.db import models
from backend.models import *
# Create your models here.
class Stats(models.Model):
    participant = models.OneToOneField(Participant)
    score = models.IntegerField()
    current_dvm_level = models.PositiveSmallIntegerField()
    current_informals_level = models.PositiveSmallIntegerField()
    level_start_time = models.DateTimeField()
    dvm_1_time = models.IntegerField()
    dvm_2_time = models.IntegerField()
    dvm_3_time = models.IntegerField()
    dvm_4_time = models.IntegerField()
    dvm_5_time = models.IntegerField()
    dvm_6_time = models.IntegerField()
    dvm_7_time = models.IntegerField()
    dvm_8_time = models.IntegerField()
    dvm_9_time = models.IntegerField()
    dvm_10_time = models.IntegerField()
    dvm_11_time = models.IntegerField()
    dvm_12_time = models.IntegerField()
