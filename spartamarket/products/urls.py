from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.product, name="product"),
    path("create/", views.create, name="create"),
]
