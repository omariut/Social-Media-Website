from django.contrib import admin
from profiles.models import Profile, Relationship,  Notification
from posts.models import Post, Comment, Like
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Relationship)
admin.site.register( Notification)
# Register your models here.
