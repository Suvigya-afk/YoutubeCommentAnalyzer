from django.db import models
from django.contrib.auth.models import User

class VideoUrl(models.Model):
    videourl = models.URLField(max_length=200)
    
class PlaylistUrl(models.Model):
    playlisturl = models.URLField(max_length=200)
