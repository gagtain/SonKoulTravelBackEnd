from django.contrib import admin
from django.utils.html import format_html

from .models import (
    CommentView,
    Photo
)

admin.site.register(Photo)


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0


@admin.register(CommentView)
class CommentViewAdmin(admin.ModelAdmin):
    list_display = ('stars', 'name', 'text', 'date')
    list_filter = ('date', 'stars')
    inlines = [PhotoInline]
