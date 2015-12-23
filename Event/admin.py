from django.contrib import admin
from .models import events, EventCategory, Tag, Heading, Tabs, organization
# Register your models here.

class EventAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'category', 'is_kernel']
	list_display_links = ['name']
	# list_filter = ['category']
	search_fields = ['name']
	def get_queryset(self, request):
	    # """Limit Pages to those that belong to the request's user."""
	    qs = super(EventAdmin, self).get_queryset(request)
	    if request.user.is_superuser:
	        # It is mine, all mine. Just return everything.
	        return qs
	    # Now we just add an extra filter on the queryset and
	    # we're done. Assumption: Page.owner is a foreignkey
	    # to a User.
	    given_org = organization.objects.get(user= request.user)
	    return qs.filter(org=given_org)

class EventCategoryAdmin(admin.ModelAdmin):
	list_display = ('name','weight',)
	list_editable = ('weight',)    


class OrgAdmin(admin.ModelAdmin):
	list_display = ('name',)
# admin.site.register(Category)
admin.site.register(events, EventAdmin)
admin.site.register(EventCategory, EventCategoryAdmin)
admin.site.register(Tag)
admin.site.register(Heading)
admin.site.register(Tabs)
admin.site.register(organization, OrgAdmin)
# admin.site.register(Notification, NotificationAdmin)