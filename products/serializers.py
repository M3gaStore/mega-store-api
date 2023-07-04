from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "value", "category", "quantity_in_stock", "is_available"]
        read_only_fields = ["id"]