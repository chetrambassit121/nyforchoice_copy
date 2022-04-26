from django.contrib import admin
from .models import Post, Comment
from . import models
from django.utils.safestring import mark_safe
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post, Comment, Notification, ThreadModel
# from members.models import UserProfile
# Register your models here.

# admin.site.register(Post)
# admin.site.register(UserProfile)
# admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(ThreadModel)




# @admin.site.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('comment', 'created_on', 'post', 'author')
    list_filter = ('comment', 'created_on', 'post', 'author')
    search_fields = ('comment', 'created_on', 'post', 'author')
admin.site.register(Comment, CommentAdmin)


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('body', 'created_on', 'author')
    list_filter = ('body', 'created_on', 'author')
    search_fields = ('body', 'created_on', 'author')
admin.site.register(Post, PostAdmin)