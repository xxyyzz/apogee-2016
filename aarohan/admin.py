from django.contrib import admin

class ResultAdmin(admin.ModelAdmin):
	readonly_fields=('id',)
	list_display = ('id','name','roll_no', 'standard','national_rank')