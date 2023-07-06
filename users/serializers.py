from rest_framework import serializers

from addresses.models import Address
from carts.models import Cart
from .models import User
from addresses.serializers import AddressSerializer


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = User
        fields = [
            "id",
            "full_name",
            "email",
            "password",
            "is_salesman",
            "username",
            "is_admin",
            "cpf",
            "address",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        address_data = validated_data.pop("address")

        address = Address.objects.create(**address_data)

        user = User.objects.create_user(address=address, **validated_data)

        Cart.objects.create(is_active=True, user=user)

        return user

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance
