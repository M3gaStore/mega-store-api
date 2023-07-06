from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from carts.models import Cart
from .serializers import CartSerializer


class CartView(ListAPIView, UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CartSerializer

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user, is_active=True)

    def get_object(self):
        user = self.request.user
        cart = Cart.objects.get(user=user, is_active=True)
        return cart
