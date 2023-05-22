from rest_framework import serializers
from .models import Comment, ShortComment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.username')
    author_image = serializers.ReadOnlyField(source='user.image.url')
    video_title = serializers.ReadOnlyField(source='video.title')

    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        

class ShortCommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.username')
    author_image = serializers.ReadOnlyField(source='user.image.url')
    short_video_title = serializers.ReadOnlyField(source='short_video.title')

    class Meta:
        model = ShortComment
        fields = '__all__'

class ShortCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortComment
        fields = '__all__'