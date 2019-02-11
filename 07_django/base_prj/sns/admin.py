from django.contrib import admin
from . import models


class PostingModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(models.Posting, PostingModelAdmin)


class CommentModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(models.Comment, CommentModelAdmin)
