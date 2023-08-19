from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser, CustomGroup, GroupPaticipant, Profile

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_admin']
    

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'date_created']

class GroupPaticipantAdmin(admin.ModelAdmin):
    list_display = ['group', 'date_joined', 'is_admin']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(CustomGroup, GroupAdmin)
admin.site.register(GroupPaticipant, GroupPaticipantAdmin)
admin.site.unregister(Group)