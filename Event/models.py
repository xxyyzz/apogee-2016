from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class EventCategory(models.Model):
	app_label='EventCategory'
	name = models.CharField(max_length = 50)
	weight = models.IntegerField(help_text= 'Heavier items sink to the bottom of the menu.')
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name_plural = 'Event Categories'


class Tag(models.Model):
    name = models.CharField(max_length = 15)
    def __unicode__(self):
        return self.name

class Organization(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length= 200, unique=True)
    cord = models.CharField(max_length=200, blank=True)
    phone= models.CharField(max_length=12, blank=True)
    email_id = models.EmailField(unique=True, null=True, blank=True)
    def __unicode__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length = 100,verbose_name = 'Event Name' ,unique = True)
    category = models.ForeignKey(EventCategory)
    tags = models.ManyToManyField(Tag,blank=True)
    short_description = models.CharField(max_length = 400)
    # contact = models.TextField(blank = 'True')
    # content = RichTextField()
   # attachments=models.FileField(blank=True,upload_to="attachments")
    # author = models.ForeignKey(User, null = True , blank = True)
    register = models.BooleanField(verbose_name = 'Enable online registration')
    is_team = models.BooleanField( verbose_name = 'Team event')
    max_participants = models.IntegerField(null = True,blank = True)
    # facebook_admin_id = models.CharField( max_length = 100 , null = True,blank = True,help_text = 'You can find your facebook id at graph.facebook.com/< your facebook username >, access admin page on your FB -> Account->Manage Pages')
    weight = models.IntegerField( null = True, blank = True)
    # date=models.CharField(max_length = 100,blank=True)
    # startingtime=models.CharField(max_length = 100,blank=True)
    # endingtime=models.CharField(max_length = 100,blank=True)
    # venue=models.CharField(max_length = 100,blank=True)
    img=models.ImageField(blank=True, upload_to="imageuploads")
    thumb=models.ImageField(blank=True, upload_to="imageuploads")
    is_kernel = models.NullBooleanField(null=True,blank=True)
    # online_reg = models.NullBooleanField(null=True,blank=True)
    org= models.ForeignKey(Organization, blank= True, null=True, default=None)
    is_displayed = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

class Schedule(models.Model):
    event= models.ForeignKey(Event)
    date=models.CharField(max_length = 100,blank=True)
    end_date=models.CharField(max_length = 100,blank=True)
    startingtime=models.CharField(max_length = 100,blank=True)
    endingtime=models.CharField(max_length = 100,blank=True)
    venue=models.CharField(max_length = 100,blank=True)
    round_no= models.CharField(max_length=100, blank=True)     


class Heading(models.Model):
    name = models.CharField(max_length = 60,unique = True)
    weight = models.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tab headings'
        verbose_name = 'Tab heading'


class Tab(models.Model):
    heading = models.ForeignKey(Heading)
    content = RichTextField()
    event = models.ForeignKey(Event)

    def __unicode__(self):
        return 'Tab for '+ self.event.name

    class Meta:
        verbose_name_plural = 'Tabs'
        verbose_name = 'Tab'
