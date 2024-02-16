from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.
class userPage(models.Model):
    '''class Status(models.TextChoices):
        ONLINE = ('ONLINE', 'Online')
        OFFLINE = ('OFFLINE', 'Offline')
    status = models.CharField(max_length = 7, choices = Status, default = Status.OFFLINE)'''
    OFFLINE = "OFF"
    ONLINE = "ON"
    CHOICES = [
        (OFFLINE, "Offline"),
        (ONLINE, "Online")
    ]
    status = models.CharField(max_length = 3, choices = CHOICES, default = OFFLINE)
    time = models.DateTimeField(default = timezone.now)
    user = models.OneToOneField(User, on_delete = models.CASCADE, default=None)

class Post(models.Model):
    tags = TaggableManager()
    body = models.CharField(max_length = 256, default = None)
    add_time = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User,on_delete = models.CASCADE, default = None)
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 250, default = None)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "comments")
    name = models.CharField(max_length = 80)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default = True)

    