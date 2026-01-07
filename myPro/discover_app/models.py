from django.db import models
from connect_app.models import UserMd

class Room(models.Model):
    client = models.ForeignKey(UserMd, on_delete= models.CASCADE, related_name= 'developers')
    developer = models.ForeignKey(UserMd, on_delete= models.CASCADE, related_name= 'clients')