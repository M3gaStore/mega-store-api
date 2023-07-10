from rest_framework import serializers

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
        extra_kwargs = {'quantity_in_stock': {'write_only': True}}

    def create(self, validated_data: dict) -> Product:
        return Product.objects.create(**validated_data)
