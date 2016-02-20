from django.contrib import admin
from ems.models import *
# Register your models here.
class ScoreAdmin(admin.ModelAdmin):
    search_fields = ['name', 'aadhaar']
    list_filter = ['is_bitsian', 'college']
    list_display = ['name', 'is_bitsian', 'aadhaar', 'email_id']
    list_editable = ['is_bitsian', 'aadhaar']
class LevelAdmin(admin.ModelAdmin):
    list_display = ['name', 'event', 'position', 'is_protected']
    list_filter = ['event']
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['team', 'level', 'judge', 'is_frozen']
    list_filter = ['judge']
class LabelAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'event']
    list_filter = ['event']
class JudgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'event']
    list_filter = ['event']

admin.site.register(Level, LevelAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Score, ScoreAdmin)
