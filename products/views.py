from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from products.filters import ProductsFilter

from products.models import Product
from products.serializers import ProductSerializer
from users.models import User
from django_filters.rest_framework import DjangoFilterBackend


class ProductsView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductsFilter

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# all products of determined user
class UserProductsView(generics.ListCreateAPIView):
    ...


# patch, delete
class SingleProductView(generics.ListCreateAPIView):
    ...
