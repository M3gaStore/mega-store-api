from products.models import Product
from products.serializers import ProductSerializer
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner, IsAdmin
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner | IsAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProductsView(generics.ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user_id = self.kwargs["pk"]
        return Product.objects.filter(owner_id=user_id)


class UserOrderView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user_id = self.kwargs["pk"]
        return Product.objects.filter(owner_id=user_id)
