from rest_framework import serializers

from users.models import User
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "street", "state", "number", "neighborhood", "zip_code"]
        read_only_fields = ["id"]

    def create(self, validated_data: dict) -> User:
        return Address.objects.create(**validated_data)