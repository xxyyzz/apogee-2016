from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

def upload_aic(self, filename):
    slugified_category = slugify(self.get_problem_statement_display())
    path = 'aic-submission/%s/%s' % (slugified_category, filename)
    return path

class AicSubmission(models.Model):
    STATEMENTS = (
    	('1', 'Shit1'),
    	('2', 'Shit2'),
    	('3', 'Shit3'),
    	('4', 'Shit4'),
    	('5', 'Shit5'),
    	('6', 'Shit6'),
    	('7', 'Shit7'),
    	('8', 'Shit8'),
    	('9', 'Shit9'),
    )
    problem_statement = models.CharField(max_length=500, choices=STATEMENTS)
    leader = models.ForeignKey('Participant', related_name='leaders')
    # college = models.ForeignKey('College')
    members = models.ManyToManyField('Participant', related_name='members', blank='True')
    solution = models.FileField(default=None, upload_to=upload_aic)
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