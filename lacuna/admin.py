from django.contrib import admin
from lacuna.models import *
# Register your models here.
class LevelAdmin(admin.ModelAdmin):
    list_display = ['level', 'dept']

admin.site.register(Participant)
admin.site.register(Level, LevelAdmin)
