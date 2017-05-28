from django.db import models

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    email = models.EmailField(unique=True)
    score = models.IntegerField(default=0)
    time = models.CharField(max_length=20)
    def __str__(self):
        return self.name
