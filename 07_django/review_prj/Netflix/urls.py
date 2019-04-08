from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:id>/", views.detail),
    path("create/", views.create),
    path("<int:id>/edit/", views.edit),
    path("<int:id>/update/", views.update),
    path("<int:id>/delete/", views.delete),
    path("new/", views.new),
]