from django.contrib import admin
from backend.models import *
from regsoft.models import *
from Event.models import *
class RoomAdmin(admin.ModelAdmin):
	readonly_fields=('id',)
	list_display = ('id','room', 'bhavan','vacancy')
class BillAdmin(admin.ModelAdmin):
	readonly_fields=('id',)
	list_display = ('id', 'participant','amount')
# class InventoryAdmin(admin.ModelAdmin):
# 	readonly_fields=('id',)
# 	list_display = ('id','gl_id','room','a','b','c','d','e','f')
# class TeamAdmin(admin.ModelAdmin):
#     list_display = ['leader', 'college']
# #admin.site.register(Bill)
admin.site.register(Bill, BillAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Bhavan)

# admin.site.register(Team, TeamAdmin)
# admin.site.register(Inventory,  InventoryAdmin)

