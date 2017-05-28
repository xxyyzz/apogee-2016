from django.contrib import admin
from aarohan.models import *

class ResultAdmin(admin.ModelAdmin):
	readonly_fields=('id',)
	list_display = ('id','name','roll_no', 'standard','national_rank')

admin.site.register(Results, ResultAdmin)