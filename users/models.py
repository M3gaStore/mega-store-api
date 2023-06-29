from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(null=True, default=False)

    address = models.ForeignKey(
        "addresses.Address", on_delete=models.PROTECT, related_name="address"
    )
