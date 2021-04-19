from django.contrib import admin

from .models import Post, Picture

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ['mission']

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_filter = ['mission']
