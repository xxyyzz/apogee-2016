from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey('Category')
    assoc = models.ForeignKey('Association')
    leader = models.ForeignKey('Participant', related_name='leaders')
    college = models.ForeignKey('College')
    members = models.ManyToManyField('Participant', related_name='members')
    upload = models.FileField()
    stub = models.CharField(max_length=5, unique=True)

class Paper(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey('Category')
    stub = models.CharField(max_length=5, unique=True)
    college = models.ForeignKey('College')
    address = models.TextField()
    author = models.ForeignKey('Participant', related_name='authors')
    co_author = models.ForeignKey('Participant', related_name='co_authors')

class Category(models.Model):
    MODELS = (
        ('Project', 'Project'),
        ('Paper', 'Paper'),
        ('Both', 'Both'),
    )
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=1, choices=MODELS)

class Association(models.Model):
    name = models.CharField(max_length=200)

class Participant(models.Model):
    name = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    email = models.EmailField(unique=True)

class College(models.Model):
    name = models.CharField(max_length=200)