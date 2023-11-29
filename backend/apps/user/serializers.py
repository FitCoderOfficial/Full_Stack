from rest_framework import serializers
from .models import User
from apps.post.serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    # Video와 ShortVideo의 시리얼라이저를 연결하여 사용자가 업로드한 비디오 및 숏 비디오의 데이터를 포함합니다.
    videos = VideoSerializer(many=True, read_only=True, source='video_set')
    videos_count = serializers.SerializerMethodField()

    short_videos = ShortVideoSerializer(many=True, read_only=True, source='shortvideo_set')
    short_videos_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ("password",)

    def get_videos_count(self, obj):
        return obj.video_set.count()
    
    def get_short_videos_count(self, obj):
        return obj.shortvideo_set.count()

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'image', 'bio')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
    
class ChangePasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField(required=True, write_only=True, min_length=5)
    password2 = serializers.CharField(required=True, write_only=True, min_length=5)

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("Password fields didn't match.")
        return data
    

class SearchUserSerializer(serializers.ModelSerializer):
    videos_count = serializers.SerializerMethodField()
    shortvideos_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "image", "bio", "videos_count","shortvideos_count")

    def get_videos_count(self, obj):
        return Video.objects.filter(uploader=obj).count()
    
    def get_shortvideos_count(self, obj):
        return ShortVideo.objects.filter(uploader=obj).count()

class UserLoggedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name", "image", "bio")


# AUTHENTICATION
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass