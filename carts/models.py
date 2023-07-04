from django.db import models


# Create your models here.
class Cart(models.Model):
    is_active = models.BooleanField()
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="cart"
    )

    product_cart = models.ManyToManyField("products.Product", through="carts.CartItem", related_name="cart_products")


class CartItem(models.Model):
    cart = models.ForeignKey("carts.Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="cart_item")

    quantity = models.IntegerField()
