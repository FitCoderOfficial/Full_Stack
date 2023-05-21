from django.contrib import admin
from .models import Comment, ShortComment

class CommentAdmin(admin.ModelAdmin):
    # list_display = ('user', 'id', )
    ordering = ('-id',)

class ShortCommentAdmin(admin.ModelAdmin):
    # list_display = ('user', 'id', )
    ordering = ('-id',)



admin.site.register(Comment, CommentAdmin)
admin.site.register(ShortComment, CommentAdmin)


