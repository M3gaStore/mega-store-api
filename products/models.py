from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    quantity_in_stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="products"
    )
