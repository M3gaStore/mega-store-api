from rest_framework import serializers

from products.models import Product
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    # product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    def to_representation(self, instance):
        print(instance.__dict__)
        x = super().to_representation(instance)
        print(x)
        return x

    class Meta:
        model = CartItem
        fields = ("id", "product", "quantity")


class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    product_cart = CartItemSerializer(many=True, write_only=True)

    def update(self, instance, validated_data):
        cart_items_data = validated_data.pop("product_cart")
        instance.cartitem_set.all().delete()

        for cart_item_data in cart_items_data:
            product_id = cart_item_data["product"]
            product_quantity = cart_item_data["quantity"]
            product = Product.objects.get(id=product_id.id)
            CartItem.objects.create(
                cart=instance, product=product, quantity=product_quantity
            )

        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()

        return instance

    class Meta:
        model = Cart
        fields = ("id", "is_active", "user", "product_cart")
