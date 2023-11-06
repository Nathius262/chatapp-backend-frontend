from django.contrib import admin
from .models import CustomGroup, GroupPaticipant, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'date_created']

class GroupPaticipantAdmin(admin.ModelAdmin):
    list_display = ['group', 'date_joined', 'is_admin']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(CustomGroup, GroupAdmin)
admin.site.register(GroupPaticipant, GroupPaticipantAdmin)