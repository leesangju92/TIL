from django.urls import path
from .models import Newsfeed, Comment
from . import views

app_name = "facebook"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:Newsfeed_id>/detail/", views.detail, name="detail"),
    path("create/", views.create, name="create")
]