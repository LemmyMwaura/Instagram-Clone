from django.contrib import admin
from .models import Post, Comment, Profile

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
