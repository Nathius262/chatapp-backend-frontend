from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import CustomUserManager
from django.urls import reverse
from .utils import pictureLocation, groupImageLocation
from django.conf import settings


# Create your models here.
class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=250, unique=True)
    username = models.CharField(verbose_name="username", max_length=250, unique=True)
    picture = models.ImageField(upload_to=pictureLocation, default="default.png", null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)      

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    @property
    def picture_url(self):
        try:
            picture = self.picture.url
        except :
            picture =""
        return picture

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    

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