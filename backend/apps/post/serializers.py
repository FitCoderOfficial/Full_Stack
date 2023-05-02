from rest_framework import serializers
from .models import * 

class VideoSerializer(serializers.ModelSerializer):
    uploader = serializers.ReadOnlyField(source='uploader.username')
    uploader_image = serializers.ReadOnlyField(source='uploader.image.url')
    uploader_id = serializers.ReadOnlyField(source='uploader.id')
    likes = serializers.SerializerMethodField()
    
    class Meta:
        model = Video
        fields = "__all__"

    def get_likes(self, obj):
        return [user.username for user in obj.likes.all()]

class ShortVideoSerializer(serializers.ModelSerializer):
    uploader = serializers.ReadOnlyField(source='uploader.username')
    uploader_image = serializers.ReadOnlyField(source='uploader.image.url')
    uploader_id = serializers.ReadOnlyField(source='uploader.id')
    likes = serializers.SerializerMethodField()
    
    class Meta:
        model = ShortVideo
        fields = "__all__"

    def get_likes(self, obj):
        return [user.username for user in obj.likes.all()]


class VideoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class ShortVideoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortVideo
        fields = "__all__"