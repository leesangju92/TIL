from django.urls import path
from . import views

app_name = "myway"

urlpatterns = [
    path("", views.myway_list, name="myway_list"),
    path("<int:id>/", views.myway_detail, name="myway_detail"),
    path("new/", views.myway_new, name="myway_new"),
    path("<int:id>/edit/", views.myway_edit, name="myway_edit"),
    path("<int:id>/delete/", views.myway_delete, name="myway_delete"),
    path("<int:posting_id>/comments/create/", views.create_comment, name="create_comment"),
    path("<int:posting_id>/comments/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"),
]