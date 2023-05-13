from rest_framework import serializers
from .models import * 
from apps.comment.serializers import CommentSerializer, ShortCommentSerializer

class VideoSerializer(serializers.ModelSerializer):
    uploader = serializers.ReadOnlyField(source='uploader.username')
    uploader_image = serializers.ReadOnlyField(source='uploader.image.url')
    uploader_id = serializers.ReadOnlyField(source='uploader.id')
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = Video
        fields = "__all__"

    def get_likes(self, obj):
        return [user.username for user in obj.likes.all()]
    
    def get_dislikes(self, obj):
        return [user.username for user in obj.dislikes.all()]

class ShortVideoSerializer(serializers.ModelSerializer):
    uploader = serializers.ReadOnlyField(source='uploader.username')
    uploader_image = serializers.ReadOnlyField(source='uploader.image.url')
    uploader_id = serializers.ReadOnlyField(source='uploader.id')
    likes = serializers.SerializerMethodField()
    dislikes = serializers.SerializerMethodField()
    short_comments = ShortCommentSerializer(many=True, read_only=True)

    
    class Meta:
        model = ShortVideo
        fields = "__all__"

    def get_likes(self, obj):
        return [user.username for user in obj.likes.all()]
    
    def get_dislikes(self, obj):
        return [user.username for user in obj.dislikes.all()]


class VideoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class ShortVideoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortVideo
        fields = "__all__"