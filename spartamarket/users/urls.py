from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("<int:user_id>/", views.profile, name="profile"),
    path("like/<int:pk>/", views.like, name="like"),
    path("<int:user_id>/follow/", views.follow, name="follow"),
    path("<int:user_id>/update_profile/", views.update_profile, name="update_profile"),
]


