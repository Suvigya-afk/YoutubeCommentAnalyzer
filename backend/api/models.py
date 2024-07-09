from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    comment_owner_username = models.CharField(max_length=50)
    posted_at = models.DateTimeField()
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return self.username
        
class VideoUrl(models.Model):
    videourl = models.URLField(max_length=200)
    
class PlaylistUrl(models.Model):
    playlisturl = models.URLField(max_length=200)
