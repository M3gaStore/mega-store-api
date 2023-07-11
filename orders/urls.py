from django.urls import path
from . import views


urlpatterns = [
    path("orders/", views.OrderView.as_view()),
    path("orders/list", views.OrderListView.as_view()),
    path("orders/sales", views.OrderSalesView.as_view()),
    path("orders/sales", views.OrderSalesView.as_view()),
]
