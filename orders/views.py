from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from carts.models import Cart
from orders.models import Order
from orders.serializers import OrderSerializer, AllOrdersSerializer


class OrderView(generics.ListAPIView, generics.UpdateAPIView, generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = AllOrdersSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer
