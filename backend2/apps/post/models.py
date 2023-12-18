from django.db import models
from apps.user.models import User

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
    tags = models.ManyToManyField(Tag, blank=True)
    view_count = models.PositiveIntegerField(default=0)
    publish_date = models.DateTimeField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name="video_likes_set", blank=True, verbose_name = "video_likes")
    dislikes = models.ManyToManyField(User, related_name="video_dislikes_set", blank=True, verbose_name = "video_dislikes")
    video_url = models.URLField(max_length=2000)  # 외부 동영상 링크
    thumbnail = models.URLField(max_length=2000, blank=True, null=True)  # 외부 썸네일 링크
    is_public = models.BooleanField(default=True)
    duration = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ('-upload_date',)
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.title

class ShortVideo(models.Model):
    title = models.CharField(max_length=255)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    view_count = models.PositiveIntegerField(default=0)
    publish_date = models.DateTimeField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name="short_video_likes_set", blank=True, verbose_name = "short_video_likes")
    dislikes = models.ManyToManyField(User, related_name="short_video_dislikes_set", blank=True, verbose_name = "short_video_dislikes")
    video_url = models.URLField(max_length=2000)  # 외부 동영상 링크
    thumbnail = models.URLField(max_length=2000, blank=True, null=True)  # 외부 썸네일 링크
    is_public = models.BooleanField(default=True)
    duration = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ('-upload_date',)
        verbose_name = "Short Video"
        verbose_name_plural = "Short Videos"

    def __str__(self):
        return self.title

    @property
    def is_short_form(self):
        return True

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