from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ('text',)
    list_filter = ('group',)

admin.site.register(Post, PostAdmin)
admin.site.register(Group)
