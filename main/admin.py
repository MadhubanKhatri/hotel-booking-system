from csv import list_dialects
from django.contrib import admin
from .models import Room, Member

# Register your models here.
# admin.site.register(Room)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_no', 'is_booked')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'room_no', 'gender')
