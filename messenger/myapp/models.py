from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class userPage(models.Model):
    '''class Status(models.TextChoices):
        ONLINE = ('ONLINE', 'Online')
        OFFLINE = ('OFFLINE', 'Offline')
    status = models.CharField(max_length = 7, choices = Status, default = Status.OFFLINE)'''
    OFFLINE = "OFF"
    ONLINE = "ON"
    CHOICES = [
        (OFFLINE,"Offline"),
        (ONLINE,"Online")
    ]
    status = models.CharField(max_length = 3, choices = CHOICES, default = OFFLINE)
    time = models.DateTimeField(default = timezone.now)
    user = models.OneToOneField(User,on_delete = models.CASCADE,default=None)


    