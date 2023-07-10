from django.db import models


class Cart(models.Model):
    is_active = models.BooleanField(default=True, blank=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="cart"
    )

    product_cart = models.ManyToManyField(
        "products.Product",
        through="carts.CartItem",
        related_name="cart_products",
        blank=True,
    )


class CartItem(models.Model):
    cart = models.ForeignKey("carts.Cart", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)

    quantity = models.IntegerField()
