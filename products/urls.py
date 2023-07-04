from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("products/", views.ProductsView.as_view()),
    path("products/<int:product_id>/", views.SingleProductView.as_view()),
    path("user/<int:user_id>/products/", views.SingleProductView.as_view())
]