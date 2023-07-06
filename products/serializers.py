from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "value",
            "category",
            "quantity_in_stock",
            "is_available",
        ]
        read_only_fields = ["id", "is_available"]

    def create(self, validated_data: dict) -> Product:
        print(validated_data)
        return Product.objects.create(**validated_data)
