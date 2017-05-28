from django.contrib import admin
from aic2016.models import *
# Register your models here.
class AicSubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'leader', 'problem_statement')
    search_fields = ['leader.name']
    filter_horizontal = ['members']
admin.site.register(AicSubmission, AicSubmissionAdmin)
admin.site.register(Participant)
