from django.contrib import admin
from .models import Newsfeed, Comment


class NewsfeedModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Newsfeed, NewsfeedModelAdmin)


class CommentModelAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Comment, CommentModelAdmin)
