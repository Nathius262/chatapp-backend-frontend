from django.db import models
from .utils import pictureLocation, groupImageLocation
from ..authentication.models import CustomUser
from django.conf import settings
from django.urls import reverse

# Create your models here.
  

class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=False, related_name="user_profile")
    name = models.CharField(verbose_name="name", max_length=500)
    picture = models.ImageField(upload_to=pictureLocation, default="default.png", null=True, blank=True)  
    
    def __str__(self):
        return str(self.user)
      
    @property
    def picture_url(self):
        try:
            picture = self.picture.url
        except :
            picture =""
        return picture

class CustomGroup(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=groupImageLocation)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GroupPaticipant(models.Model):
    group = models.ForeignKey(CustomGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return str(self.group)
    
    def get_url(self):
        return reverse('user:group_paticipant', args=[self.id])