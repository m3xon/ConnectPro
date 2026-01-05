from django.db import models
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profileImage/')
    about = models.CharField(max_length= 1000, default= '')
    skills = models.CharField(max_length= 1000, default= '')
    experience = models.CharField(max_length= 1000, default= '')
    full_name = models.CharField(max_length= 100, blank= False, default= '')
    major = models.CharField(max_length=200, default="---")
    address = models.CharField(max_length= 200, default= "---")
    active_connections = models.IntegerField(default=0)
    total_msg = models.IntegerField(default= 5)
    remain_msg = models.IntegerField(default= 5)
    reviews = models.IntegerField(default= 0)

    def __str__(self):
        return f"{self.full_name}'s Profile"
