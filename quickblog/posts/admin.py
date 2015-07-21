from django.contrib import admin

# Register your models here.
from posts.models import Post, User, UserProfile, Comment
admin.site.register(UserProfile)
