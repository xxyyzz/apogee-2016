from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

def upload_iot(self, filename):
    path = 'iot-submission/%s' % ( filename)
    return path

class IotSubmission(models.Model):
    leader = models.ForeignKey('Participant', related_name='leaders')
    # college = models.ForeignKey('College')
    members = models.ManyToManyField('Participant', related_name='members', blank='True')
    solution = models.FileField(default=None, upload_to=upload_iot)
    def __str__(self):
        return str(self.id)


class Participant(models.Model):
    name = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    email = models.EmailField(unique=True)
    college = models.CharField(max_length=200)
    yos = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.name