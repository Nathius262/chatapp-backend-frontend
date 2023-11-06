from django.conf import settings
import os

def pictureLocation(instance, filename):
    file_path = "profile/user{username}/profile.jpeg".format(
        username = str(instance.user), filename = filename,
    )
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(full_path):
        os.remove(full_path)
    return file_path

def groupImageLocation(instance, filename):
    file_path = "groups/{name}/image.jpeg".format(
        name = str(instance.name), filename = filename,
    )
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(full_path):
        os.remove(full_path)
    return file_path