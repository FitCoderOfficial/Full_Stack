from django.db import models
from apps.user.models import User
import uuid
from PIL import Image
from io import BytesIO
from django.core.files import File
from moviepy.editor import VideoFileClip
import os

def upload_video_to(instance, filename):
    # Generates a unique path for each video
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    uploader_id = instance.uploader.id if instance.uploader.id else 'unknown'
    return f"videos/{uploader_id}/{filename}"

def generate_thumbnail(video_path):
    # Generates thumbnail from the first frame of the video
    try:
        clip = VideoFileClip(video_path)
        frame = clip.get_frame(0)
        image = Image.fromarray(frame)
        thumb_io = BytesIO()
        image.save(thumb_io, format='JPEG', quality=85)
        thumbnail = File(thumb_io, name=os.path.basename(video_path) + '.jpg')
        return thumbnail
    except Exception as e:
        # Handle exceptions
        print(f"Error generating thumbnail: {e}")
        return None

class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Video(models.Model):
    title = models.CharField(max_length=255)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)  # 비디오와 관련된 태그
    duration = models.PositiveIntegerField()  # 비디오 길이 (예: 초 단위)
    view_count = models.PositiveIntegerField(default=0)  # 조회수
    likes = models.PositiveIntegerField(default=0)  # 좋아요 수
    dislikes = models.PositiveIntegerField(default=0)  # 싫어요 수
    video = models.FileField(upload_to=upload_video_to)
    thumbnail = models.ImageField(upload_to=upload_video_to, blank=True, null=True)  # 썸네일 필드 추가

    def save(self, *args, **kwargs):
        if not self.thumbnail:
            self.thumbnail = generate_thumbnail(self.video.path)
        super().save(*args, **kwargs)
    
class UserVideoInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now_add=True)
    duration_watched = models.PositiveIntegerField()
    liked = models.BooleanField(default=False)
    disliked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'video')

    def __str__(self):
        like_status = "Liked" if self.liked else "Disliked" if self.disliked else "No Reaction"
        return f'{self.user.username} - {like_status} - {self.video.title}'
