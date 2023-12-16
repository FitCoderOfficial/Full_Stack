from django.contrib import admin
from .models import User 

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'id', )
    list_filter = ('email', 'id', )
    search_fields = ('email', 'id',)
    ordering = ('-id',)

admin.site.register(User, UserAdmin)