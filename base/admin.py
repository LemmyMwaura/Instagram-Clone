from django.contrib import admin
from .models import Post, Comment, Profile, Like

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Like)
