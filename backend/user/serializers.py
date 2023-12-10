
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from .models import CustomGroup, GroupPaticipant, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['id']

class CustomGroupSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = CustomGroup
        exclude = ['id']


class GroupPaticipantSerializers(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:
        model = GroupPaticipant
        exclude = ['id']

    def get_user(self, obj):
        user_list = []
        for users in obj.user.all():
            user_list.append(users.username)
        return user_list