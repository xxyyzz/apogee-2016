from django.db import models

class Results(models.Model):
    name = models.CharField(max_length=200)
    roll_no = models.IntegerField()
    standard = models.CharField(max_length=10)
    national_rank = models.IntegerField()
    school_rank = models.IntegerField()
