from rest_framework import serializers
from .models import Order
from users.serializers import UserSerializer
from products.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ["id", "user", "product", "status", "created_at"]
