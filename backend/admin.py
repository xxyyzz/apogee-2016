from django.contrib import admin
from backend.models import *
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    filter_horizontal = ['members']

class ParticipantAdmin(admin.ModelAdmin):
    filter_horizontal = ['events', 'teams']
    search_fields = ['name']
    list_filter = ['is_bitsian', 'college']
    list_display = ['name', 'college', 'is_bitsian', 'aadhaar', 'college']
    list_editable = ['is_bitsian', 'aadhaar', 'college']


admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(College)
admin.site.register(gleader)
admin.site.register(Updates)
