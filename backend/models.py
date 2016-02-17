from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Participant(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        # ('O', 'Other'),
    )
    is_bitsian = models.BooleanField(default=False)
    user = models.OneToOneField(User, null=True)
    aadhaar = models.CharField(max_length=8, null=True, blank=True, default=None, unique=True)
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDERS)
    college = models.ForeignKey('College')
    city = models.CharField(max_length=20)
    phone_one = models.BigIntegerField()
    phone_two = models.BigIntegerField(null=True, blank=True)
    email_id = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=32, null=True, blank=True)
    social_link = models.CharField(max_length=300, null=True, blank=True)
    pcr_approval = models.BooleanField(default=False)
    events = models.ManyToManyField('Event.Event', blank=True)
    fee_paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    teams = models.ManyToManyField('Team', blank=True)

    bank_ifsc = models.CharField(max_length=11)
    bank_name = models.CharField(max_length=200)
    bank_account_no = models.CharField(max_length=20)
    address = models.TextField(max_length=1000)


    firewallzo = models.BooleanField('passed firewallz', default=False)
    # firewallzi = models.BooleanField('passed inner booth', default=False)
    recnacc = models.BooleanField('passed recnacc', default=False)
    controlz = models.BooleanField('passed controlz', default=False)

    # bill_id = models.CharField(max_length=10, default='', blank=True)
    room = models.ForeignKey('regsoft.Room',null=True,blank = True)
    class Meta:
        verbose_name_plural = 'Participants'
    def __unicode__(self):
        return str(self.name)

# ToDo: Port this model to the EMS app next time
class Team(models.Model):
    # score_set
    # levels
    name = models.CharField(max_length=200)
    members = models.ManyToManyField('Participant')
    leader = models.ForeignKey('Participant', related_name='leader_team')
    event = models.ForeignKey('Event.Event')
    rank = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
    def __unicode__(self):
        return str(self.name)

class College(models.Model):
    name = models.CharField(max_length=200)
    is_displayed = models.BooleanField(default=False)
    def __unicode__(self):
        return str(self.name)

class Updates(models.Model):
    name = models.CharField(max_length=200)
    content = RichTextField()
    date_posted = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return self.name
