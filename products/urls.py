from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("products/", views.ProductsView.as_view()),
    path("products/<int:pk>/", views.SingleProductView.as_view()),
    path("user/<int:pk>/products/", views.UserProductsView.as_view()),
]
