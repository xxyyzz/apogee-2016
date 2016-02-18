from django.db import models
# Create your models here.

# The Team model is reflected here, to be ported next time.
# class Team(models.Model):
#   # score_set
#   # levels
# 	name = models.CharField(max_length=200)
# 	members = models.ManyToManyField('Participant')
# 	leader = models.ForeignKey('Participant', related_name='leader_team')
# 	event = models.ForeignKey('Event.Event')
#   rank = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
# 	def __unicode__(self):
# 		return str(self.name)

class Score(models.Model):
    level = models.ForeignKey('Level')
    team = models.ForeignKey('backend.Team')
    judge = models.ForeignKey('Judge')
    var1 = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
    var2 = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
    var3 = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
    var4 = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
    var5 = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
    var6 = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
    var7 = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
    var8 = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
    var9 = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
    var10 = models.PositiveSmallIntegerField(default=None, null=True, blank=True)

class Level(models.Model):
    # score_set
    event = models.ForeignKey('Event.Event')
    label = models.ForeignKey('Label', null=True, blank=True)
    judges = models.ManyToManyField('Judge', blank=True)
    name = models.CharField(max_length=100)
    position = models.PositiveSmallIntegerField()
    teams = models.ManyToManyField('backend.Team', related_name='levels', blank=True)
    is_protected = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name

class Judge(models.Model):
    name = models.CharField(max_length=200)
    event = models.ForeignKey('Event.Event')
    def __unicode__(self):
        return self.name
    # score_set
    # level_set

class Label(models.Model):
    # level_set
    event = models.ForeignKey('Event.Event')
    var1name = models.CharField(max_length=100, blank=True)
    var1max = models.PositiveSmallIntegerField(default=10)
    var2name = models.CharField(max_length=100, blank=True)
    var2max = models.PositiveSmallIntegerField(default=10)
    var3name = models.CharField(max_length=100, blank=True)
    var3max = models.PositiveSmallIntegerField(default=10)
    var4name = models.CharField(max_length=100, blank=True)
    var4max = models.PositiveSmallIntegerField(default=10)
    var5name = models.CharField(max_length=100, blank=True)
    var5max = models.PositiveSmallIntegerField(default=10)
    var6name = models.CharField(max_length=100, blank=True)
    var6max = models.PositiveSmallIntegerField(default=10)
    var7name = models.CharField(max_length=100, blank=True)
    var7max = models.PositiveSmallIntegerField(default=10)
    var8name = models.CharField(max_length=100, blank=True)
    var8max = models.PositiveSmallIntegerField(default=10)
    var9name = models.CharField(max_length=100, blank=True)
    var9max = models.PositiveSmallIntegerField(default=10)
    var10name = models.CharField(max_length=100, blank=True)
    var10max = models.PositiveSmallIntegerField(default=10)
    def __unicode__(self):
        return self.event.name
