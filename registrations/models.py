from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
def upload_project(self, filename):
    slugified_category = slugify(self.category)
    path = 'projects/%s/%s' % (slugified_category, filename)
    return path

def upload_paper(self, filename):
    slugified_category = slugify(self.category)
    path = 'papers/%s/%s' % (slugified_category, filename)
    return path

#this function is of no use, however removing it hampers migrations somehow
def upload_dir(self, filename):
    slugified_category = slugify(self.category)
    path = 'papers/%s/%s' % (slugified_category, filename)
    return path

class Project(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey('Category')
    assoc = models.ForeignKey('Association')
    leader = models.ForeignKey('Participant', related_name='leaders')
    # college = models.ForeignKey('College')
    members = models.ManyToManyField('Participant', related_name='members')
    abstract = models.FileField(default=None, upload_to=upload_project)
    stub = models.CharField(max_length=8, unique=True)
    STATUSES = (
        ('0', 'Submitted'),
        ('1', 'Passed Round 1'),
        ('2', 'Passed Round 2'),
    )
    status = models.CharField(max_length=2, choices=STATUSES, default="0")
    def __unicode__(self):
        return self.name

class Paper(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey('Category')
    stub = models.CharField(max_length=8, unique=True)
    # college = models.ForeignKey('College')
    address = models.TextField()
    author = models.ForeignKey('Participant', related_name='authors')
    co_author = models.ForeignKey('Participant', related_name='co_authors', blank=True, null=True)
    abstract = models.FileField(default=None, upload_to=upload_paper)
    STATUSES = (
        ('0', 'Paper Submitted'),
        ('1', 'Cleared Round 1'),
        ('2', 'Cleared Round 2'),
    )
    status = models.CharField(max_length=2, choices=STATUSES, default="0")
    def __unicode__(self):
        return self.name

class Category(models.Model):
    MODELS = (
        ('Project', 'Project'),
        ('Paper', 'Paper'),
        ('Both', 'Both'),
    )
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=8, choices=MODELS)
    class Meta:
        verbose_name_plural = 'categories'
    def __unicode__(self):
        return self.name

class Association(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    email = models.EmailField(unique=True)
    college = models.ForeignKey('College')
    def __unicode__(self):
        return self.name

class College(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class CampusAmbassador(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    college = models.ForeignKey('College')
    year = models.CharField(max_length=20)
    degree = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField()
    ambassador_quality = models.TextField()
    root_mail = models.BooleanField(default=False)
    pcr_approved= models.NullBooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Campus Ambassadors'
    def __unicode__(self):
        return self.name

class InitialRegistration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField()
    def __unicode__(self):
        return self.name