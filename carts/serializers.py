from rest_framework import serializers

from products.models import Product
from products.serializers import ProductSerializer
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True
    )
    product_details = ProductSerializer(source="product", read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "product", "product_details", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    product_cart = CartItemSerializer(many=True, source="cartitem_set")

    def update(self, instance, validated_data):
        cart_items_data = validated_data.pop("cartitem_set")
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
