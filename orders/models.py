from django.db import models


# Create your models here.
class OrderStatusChoices(models.TextChoices):
    PEDIDO_REALIZADO = "PEDIDO REALIZADO"
    EM_ANDAMENTO = "EM ANDAMENTO"
    ENTREGUE = "ENTREGUE"


class Order(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="orders"
    )
    status = models.CharField(
        max_length=20,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.EM_ANDAMENTO,
    )
    total_value = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    product_order = models.ManyToManyField(
        "products.Product", through="orders.OrderItem", related_name="order_products"
    )


class OrderItem(models.Model):
    order = models.ForeignKey("orders.Order", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)

    quantity = models.IntegerField()
