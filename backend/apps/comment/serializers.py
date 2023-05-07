from rest_framework import serializers
from .models import Comment 

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.username')
    author_image = serializers.ReadOnlyField(source='user.image.url')
    post = serializers.ReadOnlyField(source='video.title')

    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        

