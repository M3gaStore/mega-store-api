from django.db import models


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="user"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.PROTECT, related_name="product"
    )
