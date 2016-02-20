from django.db import models
from backend.models import *
from Event.models import *

class Bhavan(models.Model):
	name=models.CharField(max_length=50)
	def __unicode__(self):
		return self.name

# class Inventory(models.Model):
# 	a = models.IntegerField(default=0, null=True)
# 	b = models.IntegerField(default=0, null=True)
# 	c = models.IntegerField(default=0, null=True)
# 	d = models.IntegerField(default=0, null=True)
# 	e = models.IntegerField(default=0, null=True)
# 	f = models.IntegerField(default=0, null=True)
# 	room = models.ForeignKey('Room', default = None)
# 	gl_id= models.IntegerField(null=True, default=0)
# 	def __unicode__(self):
# 		return str(self.room)

class Room(models.Model):
	bhavan=models.ForeignKey('Bhavan')
	room=models.CharField(max_length=50)
	vacancy=models.IntegerField()
	def __unicode__(self):
		return str(self.bhavan.name+' '+self.room)


#class bill(models.Model):
	#gleader=models.CharField(max_length=80)
	#glid= models.IntegerField(null=True)
	#amount=models.IntegerField()
	#college=models.CharField(max_length=100)
	#number = models.IntegerField()
	# notes_1000 = models.IntegerField(null=True, blank=True, default=0)
	# notes_500 = models.IntegerField(null=True, blank=True, default=0)
	# notes_100 = models.IntegerField(null=True, blank=True, default=0)
	# notes_50 = models.IntegerField(null=True, blank=True, default=0)
	# notes_20 = models.IntegerField(null=True, blank=True, default=0)
	# notes_10 = models.IntegerField(null=True, blank=True, default=0)
	#def __unicode__(self):
		#return str(self.number)

# class Bill(models.Model):
	# gleader=models.CharField(max_length=80)
	# amount=models.IntegerField()
	# college=models.CharField(max_length=100)
	# number = models.IntegerField()
	#draft_number = models.CharField(max_length=100)
	# def __unicode__(self):
		# return str(self.number)
		
class Bill(models.Model):
	gleader = models.CharField(max_length=10, null=True,blank=True)
	amount = models.IntegerField(default=0)
	given=models.IntegerField(default =0)
	balance=models.IntegerField( default=0)

	notes_1000 = models.IntegerField(null=True, blank=True, default=0)
	notes_500 = models.IntegerField(null=True, blank=True, default=0)
	notes_100 = models.IntegerField(null=True, blank=True, default=0)
	notes_50 = models.IntegerField(null=True, blank=True, default=0)
	notes_20 = models.IntegerField(null=True, blank=True, default=0)
	notes_10 = models.IntegerField(null=True, blank=True, default=0)

	#number = models.IntegerField()
	draft_number = models.CharField(max_length=100, default='')
	def __unicode__(self):
		return str(self.id)
		
# class Team(models.Model):
# 	event =  models.ForeignKey(Event)
# 	bitsian_members = models.ManyToManyField(Bitsian, blank=True, related_name='member_set')
# 	members = models.ManyToManyField(InitialRegistration, blank=True, related_name='member_set')
# 	bitsian_leader = models.ForeignKey(Bitsian, null=True, blank=True)
# 	leader = models.ForeignKey(InitialRegistration, null=True, blank=True)
# 	college = models.ForeignKey(College)
# 	is_finalist = models.BooleanField(default=False)
# 	is_winner = models.BooleanField(default=False)
# 	address = models.CharField(max_length=200, null=True, blank=True)
# 	name_cheque = models.CharField(max_length=100, null=True, blank=True)
# 	position = models.IntegerField(null=True, blank=True)
# 	category = models.CharField(max_length=200, null=True, blank=True)