from django.contrib import admin
from .models import events, EventCategory, Tag, Heading, Tabs
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'is_kernel']
    list_display_links = ['name']
    # list_filter = ['category']
    search_fields = ['name']

# admin.site.register(Category)
admin.site.register(events, EventAdmin)
admin.site.register(EventCategory)
admin.site.register(Tag)
admin.site.register(Heading)
admin.site.register(Tabs)
# admin.site.register(Notification, NotificationAdmin)