from django.contrib import admin
from .models import Event, Category
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'is_kernel']
    list_display_links = ['name']
    # list_filter = ['category']
    search_fields = ['name']

# admin.site.register(Category)
admin.site.register(Event, EventAdmin)
admin.site.register(Category)
# admin.site.register(Notification, NotificationAdmin)