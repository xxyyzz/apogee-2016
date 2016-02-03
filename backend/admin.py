from django.contrib import admin
from backend.models import *
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    filter_horizontal = ['members']

class ParticipantAdmin(admin.ModelAdmin):
    filter_horizontal = ['events', 'teams']

admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(College)
admin.site.register(Updates)
