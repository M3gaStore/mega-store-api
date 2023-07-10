from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True)
    is_salesman = models.BooleanField(null=True, default=False)
    is_admin = models.BooleanField(null=True, default=False)
    cpf = models.CharField(max_length=11, unique=True)

    address = models.ForeignKey(
        "addresses.Address", on_delete=models.PROTECT, related_name="address"
    )
