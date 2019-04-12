from django.urls import path
from . import views

app_name = "foods"

urlpatterns = [
    path("", views.food_list, name="food_list"),
    path("<int:food_id>/", views.food_detail, name="food_detail"),
    path("<int:food_id>/update/", views.update_food, name="update_food"),
    path("create/", views.create_food, name="create_food"),
]
