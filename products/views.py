from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from products.filters import ProductsFilter
from products.models import Product
from products.serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend

from users.permissions import IsSalesmanOrReadOnly


class ProductsView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductsFilter

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsSalesmanOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# patch, delete
class SingleProductView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# all products of determined user
class UserProductsView(generics.ListCreateAPIView):
    ...
