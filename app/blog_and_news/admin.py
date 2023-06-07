from django.contrib import admin
from django_summernote import admin as sadmin

from .models import BlogNews

@admin.register(BlogNews)
class BlogNewsAdmin(sadmin.SummernoteModelAdmin):
    summernote_fields = ('content',)
