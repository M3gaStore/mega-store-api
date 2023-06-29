from rest_framework import serializers
from .models import User
from addresses.serializers import AddressSerializer


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "full_name", "email", "is_superuser", "address"]
