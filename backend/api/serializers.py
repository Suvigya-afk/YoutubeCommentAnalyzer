from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Comment, VideoUrl, PlaylistUrl

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "comment_owner_username", "posted_at", "comment"]
        extra_kwargs = {"author": {"read_only": True}}
        
class VideoUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoUrl
        fields = ["videourl"]

class PlaylistUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistUrl
        fields = ["playlisturl"]