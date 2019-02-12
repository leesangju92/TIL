from django.contrib import admin
from .models import Movie


class MovieModelAdmin(admin.ModelAdmin):
    readonly_fields = ("create_at", "update_at")


admin.site.register(Movie, MovieModelAdmin)
