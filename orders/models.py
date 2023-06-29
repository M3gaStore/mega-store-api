from django.db import models


# Create your models here.
class OrderStatusChoices(models.TextChoices):
    PEDIDO_REALIZADO = "PEDIDO REALIZADO"
    EM_ANDAMENTO = "EM ANDAMENTO"
    ENTREGUE = "ENTREGUE"


class Order(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="user"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.PROTECT, related_name="product"
    )
    status = models.CharField(
        max_length=20,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.EM_ANDAMENTO,
    )
    created_at = models.DateTimeField(auto_now_add=True)
