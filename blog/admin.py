from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "status")
    search_fields = ["title", "content"]
    list_filters = ("status", "created_on",)
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)

# Register your models here.

admin.site.register(Comment)
