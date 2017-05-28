from django.contrib import admin
from .models import Event, EventCategory, Tag, Heading, Tab, Organization, Schedule
# Register your models here.

class EventAdmin(admin.ModelAdmin):
	list_display = ['id', 'name','org', 'category', 'is_kernel']
	list_display_links = ['name']
	search_fields = ['name']
	def get_queryset(self, request):
		# """Limit Pages to those that belong to the request's user."""
		qs = super(EventAdmin, self).get_queryset(request)
		if request.user.is_superuser or request.user.username == 'junioradmin':
			# It is mine, all mine. Just return everything.
			return qs
		# Now we just add an extra filter on the queryset and
		# we're done. Assumption: Page.owner is a foreignkey
		# to a User.
		given_org = Organization.objects.get(user= request.user)
		return qs.filter(org=given_org)


class TabAdmin(admin.ModelAdmin):
	list_display = ['heading', 'event']
	search_fields = ['event']
	# list_display_links = ['name']
	# list_filter = ['category']
	# search_fields = ['event.name']
	def get_queryset(self, request):
		# """Limit Pages to those that belong to the request's user."""
		qs = super(TabAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			# It is mine, all mine. Just return everything.
			return qs
		# Now we just add an extra filter on the queryset and
		# we're done. Assumption: Page.owner is a foreignkey
		# to a User.
		given_org = Organization.objects.get(user= request.user)
		events_list = Event.objects.filter(org=given_org)
		return qs.filter(event__in=events_list)
		# tabs_list=qs.filter(event__in=events_list)
		# c=0
		# for event in events_list:
		# 	if c==0:
		# 		continue
		# 	c+=1
		# 	tabs_list= tabs_list + qs.filter(event= event)

		# return tabs_list


class EventCategoryAdmin(admin.ModelAdmin):
	list_display = ('name','weight',)
	list_editable = ('weight',)


class OrgAdmin(admin.ModelAdmin):
	list_display = ('user','name','cord')

class ScheduleAdmin(admin.ModelAdmin):
	list_display = ['event', 'date','round_no']	
# admin.site.register(Category)
admin.site.register(Event, EventAdmin)
admin.site.register(EventCategory, EventCategoryAdmin)
admin.site.register(Tag)
admin.site.register(Heading)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Tab, TabAdmin)
admin.site.register(Organization, OrgAdmin)
# admin.site.register(Notification, NotificationAdmin)
