from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="음악 API")


urlpatterns = [
    path("", schema_view),
    path("songs/", views.song_list),
    path("songs/<int:song_id>/", views.song_detail),
    path("songs/create/", views.create_song),
]