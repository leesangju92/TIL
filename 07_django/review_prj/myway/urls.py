from django.urls import path
from . import views

app_name = "myway"

urlpatterns = [
    path("", views.myway_list, name="myway_list"),
    path("<int:id>/", views.myway_detail, name="myway_detail"),

]