from django.contrib import admin
from .models import Video, ShortVideo

class PostAdmin(admin.ModelAdmin):
    list_display = ('uploader', 'id', )
    ordering = ('-id',)

admin.site.register(Video, PostAdmin)
admin.site.register(ShortVideo, PostAdmin)