from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.product, name="product"),
    path("create/", views.create, name="create"),
    path("<int:pk>/delete", views.delete, name="delete"),
    path("<int:pk>/", views.product_detail, name = "product_detail"),
]
