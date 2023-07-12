from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from orders.models import Order
from orders.serializers import (
    OrderSerializer,
    AllOrdersSerializer,
    UpdateOrderSerializer,
)
from users.permissions import IsAccountOwner, IsAdmin, IsSalesman
from django.core.mail import send_mail
from django.conf import settings


class OrderView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner | IsSalesman | IsAdmin]

    serializer_class = AllOrdersSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer


class OrderListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner | IsSalesman | IsAdmin]

    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)


class OrderSalesView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSalesman | IsAdmin]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSalesman | IsAdmin]

    queryset = Order.objects.all()
    serializer_class = UpdateOrderSerializer

    send_mail(
        subject="Order atualizada",
        message="Email enviado",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=False,
    )
