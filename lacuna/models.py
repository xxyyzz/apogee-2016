from django.db import models
from backend.models import *
from django.http import JsonResponse
# Create your models here.
class Participant(models.Model):
    fbid = models.BigIntegerField()
    name = models.CharField(max_length=200)
    progress = models.IntegerField(default=0)
    current_dvm_level = models.PositiveSmallIntegerField(default=1)
    start_time = models.DateTimeField()
    total_time = models.DurationField(null=True, blank=True)
    dvm_1_time = models.DurationField(null=True, blank=True)
    dvm_2_time = models.DurationField(null=True, blank=True)
    dvm_3_time = models.DurationField(null=True, blank=True)
    dvm_4_time = models.DurationField(null=True, blank=True)
    dvm_5_time = models.DurationField(null=True, blank=True)
    dvm_6_time = models.DurationField(null=True, blank=True)
    dvm_7_time = models.DurationField(null=True, blank=True)
    dvm_8_time = models.DurationField(null=True, blank=True)
    dvm_9_time = models.DurationField(null=True, blank=True)
    dvm_10_time = models.DurationField(null=True, blank=True)
    dvm_11_time = models.DurationField(null=True, blank=True)
    dvm_12_time = models.DurationField(null=True, blank=True)
    informals_stats = models.CharField(max_length=100, default='000000000000')
    def __str__(self):
        return self.name

class Level(models.Model):
    DEPARTMENTS = (
    ('DVM', 'DVM'),
    ('INFORMALS', 'INFORMALS'),
    )
    dept = models.CharField(max_length=10, choices=DEPARTMENTS)
    level = models.PositiveSmallIntegerField()
    js_file = models.TextField(default='NA')
    html_file = models.TextField(default='NA')
    css_file = models.TextField(default='NA')
    answer = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return str(self.level)
