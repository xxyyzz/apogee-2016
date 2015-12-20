from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name=models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name_plural = 'categories'
    def __unicode__(self):
        return  self.name
 
class Event(models.Model):
    name = models.CharField(max_length=100,unique=True)
    content = RichTextField()
    short_description = models.CharField(blank=True,max_length=140)
    description = models.CharField(blank=True,max_length=200)
    category = models.ForeignKey('Category')
    is_kernel = models.BooleanField(default=False)
    icon = models.ImageField(blank=True, upload_to="icons")
    date = models.CharField(max_length=100, default='TBA')
    time = models.CharField(max_length=100, default='TBA')
    venue = models.CharField(max_length=100, default='TBA')
    def __unicode__(self):
        return self.name

# class Notification(models.Model):
#     TYPES=(
#         ('static','static'),
#         ('internal','internal'),
#         ('external','external'),
#     )
#     content = RichTextField()
#     types = models.CharField(max_length=20, choices=TYPES, default='static')
#     link = models.CharField(max_length=50, default='None')
#     def __unicode__(self):
#         return self.link