from django.db.models.signals import post_save
from .models import GroupPaticipant, CustomGroup, Profile
from ..authentication.models import CustomUser


def create_group_paticipant(sender, instance, *args, **kwargs):
    paticipant_admin = GroupPaticipant.objects.all().get_or_create(group=instance, user=instance.user, is_admin=True)
    return paticipant_admin

def create_user_profile(sender, instance, created, *args, **kwargs):
    user = instance
    if created:
        print(f"creating {user}!")
        Profile(user=user)


post_save.connect(create_user_profile, sender=CustomUser)
post_save.connect(create_group_paticipant, sender=CustomGroup)