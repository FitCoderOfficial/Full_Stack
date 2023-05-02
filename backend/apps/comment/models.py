from django.db import models
from apps.post.models import Video, ShortVideo
from django.contrib.auth import get_user_model

class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["-pk"]
    def __str__(self):
        return f"{self.user}님이 {self.video.title}글에 댓글을 남겼습니다."
    
class Short_Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    video = models.ForeignKey(ShortVideo, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Short_Comment"
        verbose_name_plural = "Short_Comments"
        ordering = ["-pk"]
    def __str__(self):
        return f"{self.user}님이 {self.video.title}글에 댓글을 남겼습니다."