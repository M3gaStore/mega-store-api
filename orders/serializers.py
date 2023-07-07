from rest_framework import serializers

from carts.models import Cart, CartItem
from products.models import Product
from .models import Order, OrderItem
from users.serializers import UserSerializer
from products.serializers import ProductSerializer
from rest_framework.exceptions import ValidationError


class OrderntemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True
    )
    product_details = ProductSerializer(source="product", read_only=True)

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = OrderntemSerializer(many=True, read_only=True, source="orderitem_set")

    class Meta:
        model = Order
        fields = ["id", "user", "product", "status", "created_at", "total_value"]
        read_only_fields = [
            "id",
            "user",
            "product",
            "status",
            "created_at",
            "total_value",
        ]


class AllOrdersSerializer(serializers.Serializer):
    pedidos = OrderSerializer(read_only=True, many=True)

    def create(self, validated_data):
        retorno = []
        cart = Cart.objects.get(user=validated_data["user"], is_active=True)
        products = CartItem.objects.filter(cart_id=cart.id)
        if len(products) == 0:
            raise ValidationError(
                "Não é possivel criar um pedido com o carrinho vazio!"
            )
        owners_list = []
        products_list = []
        for product in products:
            product_detail = Product.objects.get(id=product.product_id)
            if (
                product.quantity > product_detail.quantity_in_stock
                or not product_detail.is_available
            ):
                raise ValidationError(
                    "O estoque não possui essa quantidade de item ou o item está indisponivel."
                )
            else:
                product_detail.quantity_in_stock -= product.quantity
                product_detail.save()
            products_list.append(product_detail)
            if product_detail.owner not in owners_list:
                owners_list.append(product_detail.owner)
        index = 0
        for owner in owners_list:
            total = 0
            order = Order.objects.create(user=validated_data["user"], total_value=0)
            for i, product in enumerate(products_list):
                if product.owner.id == owner.id:
                    OrderItem.objects.create(
                        quantity=products[index].quantity, order=order, product=product
                    )
                    total += products[index].quantity * product.value
                    del products_list[i]
                index += 1
            order.total_value = total
            order.save()
            retorno.append(order)
        cart.is_active = False
        cart.save()
        Cart.objects.create(is_active=True, user=validated_data["user"])

        response_data = {"pedidos": retorno}
        return response_data
