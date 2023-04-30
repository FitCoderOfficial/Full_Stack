from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    # list_display = ('user', 'id', )
    ordering = ('-id',)

admin.site.register(Comment, CommentAdmin)