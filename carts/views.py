from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from carts.models import Cart
from .serializers import CartSerializer


class CartView(generics.ListAPIView, generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartSerializer

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user, is_active=True)

    def get_object(self):
        user = self.request.user
        cart = Cart.objects.get(user=user, is_active=True)
        return cart
