from django.urls import path
from . import views

app_name="sns"

urlpatterns = [
    path("", views.posting_list, name="posting_list"),
    path("<int:posting_id>/", views.posting_detail, name="posting_detail"),
    path("new/", views.create_posting, name="create_posting"),
    path("<int:posting_id>/edit/", views.posting_edit, name="posting_edit"),
    path("<int:posting_id>/delete/", views.posting_delete, name="posting_delete"),
    path("<int:posting_id>/create_comment/", views.create_comment, name="create_comment"),
]

