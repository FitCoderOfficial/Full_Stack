from django.db import models
from django.contrib.auth.models import AbstractUser

def user_image(instance, filename):
    return f'user/{instance.username}/{filename}'

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    image = models.ImageField(upload_to=user_image, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'