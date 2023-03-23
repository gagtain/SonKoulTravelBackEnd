from django.contrib import admin
from django.utils.html import format_html

from .models import CommentView


class CommentViewAdmin(admin.ModelAdmin):
    list_display = ('stars', 'name', 'text', 'image', 'created_at')
    list_filter = ('created_at', 'stars')

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px;"/>'.format(obj.image.url))

    image_preview.short_description = 'image'
